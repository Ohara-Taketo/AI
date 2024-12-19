import json

# フィルタIDとカテゴリIDが一致した場合、取り出し
# json.loads()とjson()はどちらもjsonデータをpython形式に変更するが、json()はrequestsライブラリで使用されるメソッド
# loads()は文字列を引数にとり、load()はファイルオブジェクト型を引数にとる
# spots:施設情報の詰まったリスト

# フィルタされた施設一覧を返す
def filter(spots, fil_ids):
    # フィルタ結果リスト
    response = []
    spots = json.loads(spots)["data"]
    for spot in spots:
        # フィルタIDとカテゴリIDの数字部分が一致した場合、リストに追加
        # リスト同士で一致する要素があるか確認
        if set([fil_id[1:] for fil_id in fil_ids]) & set([category[1:] for category in spot["category"]]):
            response.append({
            "spot_id": spot["spot_id"],
            "name": spot["name"],
            "identification": spot["identification"]
            })
    return json.dumps(response)
