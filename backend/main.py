from fastapi import FastAPI, Query, Body
from fastapi.middleware.cors import CORSMiddleware
import json
from typing import Optional, Any
from datetime import datetime
from filter import filter
from sort import sort
from limit import limit
import KamiGo_http
from load_json import load_json

app = FastAPI()

# 通信するreactなどのアプリのURL
# フィルタはいろんなところで使うかもなので、その際はちゃんとその使用するところのURLをリストに入れよう
# AIトラベルなどは「http://localhost:3000/AItravel」ってなってるかもね
origins = [
    "http://localhost:3000", 
]

# 最初にfastapiからCORSMiddlewareを読み込んだ後に、URL別にアクセスできる権限を付与している
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 「@app.get("/")」は「/」というURLにGetリクエスト来たら、という意味
# 「/」はデフォルトのURL
# 「http://127.0.0.1:8000/」がデフォルト
# 「http://127.0.0.1:8000/」は「uvicorn main:app --reload」と打ち、起動したサーバのURL
# 「/run-filter」は「http://127.0.0.1:8000/run-filter」
@app.post("/run-filter")
def Filter(
    # キー指定おなしゃす
    input_data: Optional[dict[str, Any]] = Body(None), # 必須でない
    filter_mode: str = Query(None), # 必須でない("filter"or"search")
    filter_type: str = Query("or"), # 必須でない
    input_filterIDs: list[str] = Query([]), # 必須でない
    input_text: str = Query(""), # 必須でない
    sort_key: str = Query(None), # 必須でない
    limit_number: int = Query(None) # 必須でない
):
    # ボディデータが空の場合のデフォルト値
    if input_data is None:
        input_data = {"data": []}
    data = json.dumps(input_data)
    # フィルタIDリストを変形
    if input_filterIDs:
        input_filterIDs = input_filterIDs[0].split(",")
    if filter_mode is not None:
        data = filter(data, filter_mode, filter_type, input_filterIDs, input_text)
    if sort_key is not None:
        data = sort(data, sort_key)
    if limit_number is not None:
        data = limit(data, limit_number)
    # FastAPIでは、returnにjson形式で書くだけで、jsonデータでレスポンスを送る事ができる
    return {"data": json.loads(data)["data"]}

@app.post("/run-workflow")
def Filter(
    main_spotID: str,
    input_data: Optional[dict[str, Any]] = Body(...), # 必須
    filter_type: str = Query("or"), # 必須でない
    input_filterIDs: list[str] = Query([]), # 必須でない
    input_travel_start: str = None,
    input_travel_end: str = None,
):
    # ナレッジ更新用のデータ作成
    main_spot = [spot["name"] for spot in input_data["data"] if spot["spot_id"] == main_spotID][0]

    if input_filterIDs:
        input_filterIDs = input_filterIDs[0].split(",")
    above90_filterIDs = [filterID for filterID in input_filterIDs if int(filterID[1:]) > 90]
    filterIDs = [filterID for filterID in input_filterIDs if int(filterID[1:]) <= 90]
    data = json.dumps(input_data)
    data = filter(data, "filter", filter_type, filterIDs, "")
    if above90_filterIDs:
        # フィルタIDデータベースがあればif文を簡略化可能だよん
        if above90_filterIDs[0] == "f091":
            sort_key = "KUT"
        data = sort(data, sort_key)
    data = f"香美市観光地一覧:{str(json.loads(data)["data"])}"
    travel_start = datetime.strptime(input_travel_start, "%Y-%m-%d")
    travel_end = datetime.strptime(input_travel_end, "%Y-%m-%d")
    if travel_start < travel_end:
        difference = travel_end - travel_start
        schedule = f"{difference.days - 1}泊{difference.days}日"
    elif travel_start > travel_end:
        difference = travel_start - travel_end
        schedule = f"{difference.days - 1}泊{difference.days}日"
    else:
        schedule = "日帰り"
    if schedule == "0泊1日":
        schedule = "日帰り"
    # ナレッジ更新
    payload = json.dumps({
    "name": "香美市観光地一覧.txt",
    "text": data,
    "indexing_technique": "high_quality",
    "process_rule": {
    "mode": "automatic"
    }
    })
    api_key_knowledge = "dataset-SSOsOVMRui8xNfjV1YE3sjpG"
    dataset_id = "162cffa8-8dbc-4508-bee2-077c5b6921e4"
    document_id = "a4f23c38-99ac-4348-9404-68d62ea91b04"
    KamiGo_http.update_dify_knowledge(api_key_knowledge, dataset_id, document_id, payload)
    # ワークフロー実行
    inputs = {
    "Input_Order": "高知県香美市のおすすめ観光地",
    "Input_MainSpot": main_spot,
    "Input_Spot_Identification": "香美市観光地",
    "Input_Schedule": schedule,
    } # ここに質問を入れる
    api_key_KamiGo = "app-2illI1Ol6WgATS94Wld7efZW"
    response = KamiGo_http.run_dify_workflow(api_key_KamiGo, inputs, "blocking", "KamiGo_admin")
    print(response)
    return {"data": response["data"]["outputs"]}

@app.get("/get-data")
def Get_data():
    return json.loads(load_json())