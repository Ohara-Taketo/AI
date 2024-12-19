import json

# 観光地の検索結果を返す
def search(spots, input_text):
    # 検索結果リスト
    response = []
    spots = json.loads(spots)
    for spot in spots:
        if (spot["name"]).find(input_text.lower()) != -1:
            response.append({
            "spot_id": spot["spot_id"],
            "name": spot["name"],
            "identification": spot["identification"]
            })
    return json.dumps(response)