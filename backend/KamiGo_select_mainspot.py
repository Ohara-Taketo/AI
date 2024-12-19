import json

# メインスポットの情報を返す
def select_mainspot(spots, spot_id):
    spots = json.loads(spots)
    for spot in spots:
        if spot["spot_id"] == spot_id:
            response = {
            "spot_id": spot["spot_id"],
            "name": spot["name"],
            "identification": spot["identification"]
            }
    return json.dumps(response)