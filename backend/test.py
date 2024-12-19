import requests
import json
import ndjson
import KamiGo_extraction_weather
import KamiGo_http
from pykakasi import kakasi


# 動く
# url = 'https://news.yahoo.co.jp'
# response = requests.get(url)
# print(response.text[:500])

# 動く
# url = "https://www.jma.go.jp/bosai/forecast/data/forecast/190000.json"
# response = requests.get(url).json()
# print(response)

# 動かない
# def get_weather(area_code):
#     url = "https://www.jma.go.jp/bosai/forecast/data/forecast/{area_code}.json"
#     response = requests.get(url).json()
#     print(response)

# get_weather(190000)

# 動く
# def get_weather(url):
#     response = requests.get(url).json()
#     print(response)

# get_weather("https://www.jma.go.jp/bosai/forecast/data/forecast/190000.json")


# def get_weather(area_code):
#     url = f"https://www.jma.go.jp/bosai/forecast/data/forecast/{area_code}.json"
#     response = requests.get(url, timeout = 5)

#     if response.status_code == 200:
#         result = response.json()
#     else:
#         result = f"Request failed with status code {response.status_code}"
#     return result

# print(get_weather(190000))

# with open('sightseeing_spot.ndjson', encoding='UTF-8') as f:
#     input_data = ndjson.load(f)[0]
#     table = str.maketrans({
#     "'": '"',
#     })
#     print_data = input_data.translate(table)
#     print(print_data)

# with open('sightseeing_spot.ndjson') as f:
#     input_data = ndjson.dumps(f)
#     input_data = input_data.replace("'", '"')
#     input_data = ndjson.load(input_data)
#     print(input_data)

# ファイルを開いて、内容を読み込む
# with open('sightseeing_spot.ndjson') as f:
#     input_data = ndjson.load(f)
#     json_input_data = json.dumps(input_data, ensure_ascii=False, indent=2)

# print(json_input_data)

# with open('sightseeing_spots.json') as f:
#     input_data = json.load(f)

# print(input_data)

# file_path = "sightseeing_spots.json"

# # jsonファイルを読み込んで表示する
# with open(file_path, "r", encoding="utf-8") as f:
#     data_list = json.load(f)  # ファイルの内容を読み込む。loadならfだけ。loadsならf.read()。
#     print(json.dumps(data_list, ensure_ascii=False, indent=4))


# 香美市（高知県中部）の週間天気予報JSONデータのURL
# url = 'https://www.jma.go.jp/bosai/forecast/data/forecast/390000.json'
# response = requests.get(url)

# # JSON形式のデータを取得
# if response.status_code == 200:
#     forecast_data = response.json()
    
#     # 取得データの表示
#     print(json.dumps(forecast_data, indent=4, ensure_ascii=False))
# else:
#     print("データの取得に失敗しました。")


# print(KamiGo_extraction_weather.extraction_weather(390000))
# spot = "べふ峡"
# address = "香美市土佐山田"
# api_key = "dataset-SSOsOVMRui8xNfjV1YE3sjpG"
# dataset_id = "162cffa8-8dbc-4508-bee2-077c5b6921e4"
# data = {
#         "香美市観光地名": spot,
#         "response_mode": address
#     }
# print(Dify_update_data_http.update_dify_knowledge(api_key, dataset_id, data))

# import requests
# import json

# url = "https://api.dify.ai/v1/datasets/162cffa8-8dbc-4508-bee2-077c5b6921e4/document/create-by-text"

# payload = json.dumps({
# "name": "text",
# "text": "text",
# "indexing_technique": "high_quality",
# "process_rule": {
# "mode": "automatic"
# }
# })
# headers = {
# 'Authorization': 'Bearer dataset-SSOsOVMRui8xNfjV1YE3sjpG',
# 'Content-Type': 'application/json'
# }

# response = requests.request("POST", url, headers=headers, data=payload)

# print(response.text)

# ナレッジ更新テスト
# payload = json.dumps({
# "name": "テスト",
# "text": "これはテストです",
# "indexing_technique": "high_quality",
# "process_rule": {
# "mode": "automatic"
# }
# })
# api_key = "dataset-SSOsOVMRui8xNfjV1YE3sjpG"
# dataset_id = "162cffa8-8dbc-4508-bee2-077c5b6921e4"
# document_id = "3ef45aa1-30e8-4f59-9569-ed8299ec5cb8"
# KamiGo_http.update_dify_knowledge(api_key, dataset_id, document_id, payload)

# inputs = {
# "Input": "日本の首都はどこ"
# } #　ここに質問を入れる
# print(KamiGo_http.run_dify_workflow("app-EplueTJQGhoUZcS2Ek9PgLpm", inputs, "blocking", "KamiGo_admin"))

# kakasi_instance = kakasi()
# # モードの設定
# # J(Kanji) to H(Hiragana)
# kakasi_instance.setMode("J", "H")
# # 変換器の用意
# convJtoH = kakasi_instance.getConverter()
# # H(Hiragana) to E(JIS ROMAN)
# kakasi_instance.setMode("H", "E")
# convHtoE = kakasi_instance.getConverter()

# # アルファベットは小文字に変換
# print(convHtoE.do(convJtoH.do("べふ峡")).lower())
# print(convHtoE.do(convJtoH.do("be")).lower())

# from load_json import load_json
# from sort import sort

# print(sort("on", "KUT", load_json()))
# input_filterIDs=["f001"]
# above90_filterIDs = [filterID for filterID in input_filterIDs if int(filterID[1:]) > 90]
# filterIDs = [filterID for filterID in input_filterIDs if int(filterID[1:]) <= 90]
# print(above90_filterIDs)
# print(filterIDs)

# from datetime import datetime
# input_travel_start = "2024-12-16"
# input_travel_end = "2024-12-16"
# travel_start = datetime.strptime(input_travel_start, "%Y-%m-%d")
# travel_end = datetime.strptime(input_travel_end, "%Y-%m-%d")
# if travel_start < travel_end:
#     difference = travel_end - travel_start
#     schedule = f"{difference.days - 1}泊{difference.days}日"
# elif travel_start > travel_end:
#     difference = travel_start - travel_end
#     schedule = f"{difference.days - 1}泊{difference.days}日"
# else:
#     schedule = "日帰り"
# if schedule == "0泊1日":
#     schedule = "日帰り"
# print(schedule)

inputs = {
"Input_Order": "高知県香美市のおすすめ観光地",
"Input_MainSpot": "アンパンマンミュージアム",
"Input_Spot_Identification": "香美市観光地",
"Input_Schedule": "日帰り",
} # ここに質問を入れる
api_key_KamiGo = "app-2illI1Ol6WgATS94Wld7efZW"
response = KamiGo_http.run_dify_workflow(api_key_KamiGo, inputs, "blocking", "KamiGo_admin")
print(response["data"]["outputs"])