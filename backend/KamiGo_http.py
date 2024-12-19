import requests
import json

# 気象庁から天気を取得
def get_weather(area_code):
    url = f"https://www.jma.go.jp/bosai/forecast/data/forecast/{area_code}.json"
    # 気象情報の取得
    response = requests.get(url, timeout = 5)
    # 成功時jsonデータを返す
    if response.status_code == 200:
        # jsonデータを返す
        response = response.json()
    else:
        response = f"Request failed with status code {response.status_code}"
    return response

# difyのナレッジ更新
def update_dify_knowledge(api_key, dataset_id, document_id, payload):
    url = f"https://api.dify.ai/v1/datasets/{dataset_id}/documents/{document_id}/update-by-text"
    headers = {
    'Authorization': f'Bearer {api_key}',
    'Content-Type': 'application/json'
    }
    # ナレッジの更新
    response = requests.post(url, headers = headers, data = payload, timeout = 20)
    # うまくいった場合と行かなかった場合の対応
    if response.status_code == 200:
        response = "Knowledge update succeed"
    else:
        response = f"Request failed with status code {response.status_code}"
    print(response)

# difyのワークフロー実行
def run_dify_workflow(api_key, inputs, response_mode, user):
    # Content-Typeの設定(「text/event-stream」どこ？ここ？)
    # if response_mode == "blocking":
    #     Content_Type = "application/json"
    # elif response_mode == "streaming":
    #     Content_Type = "text/event-stream"
    url = "https://api.dify.ai/v1/workflows/run"
    headers = {
    'Authorization': f'Bearer {api_key}',
    'Content-Type': 'application/json'
    }
    payload = json.dumps({
    "inputs": inputs,
    "response_mode": response_mode,
    "user": user
    })
    # ワークフローの実行
    response = requests.post(url, headers = headers, data = payload, timeout = 20)
    # 返すデータの準備
    if response.status_code == 200:
        if response_mode == "blocking":
            response = response.json()
        elif response_mode == "streaming":
            # chunk_size=Noneの場合、streamの値に応じて異なる動作をする
            for chunk in response.iter_content(chunk_size = None):
                # chunkに何か入っていればTrueとなる
                if chunk:
                    response = chunk.decode()
    else:
        print(headers)
        response = f"Request failed with status code {response.status_code}"
    return response