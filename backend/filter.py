import json
from pykakasi import kakasi


def filter(input_data, filter_mode, filter_type, input_filterIDs, input_text):
    # フィルタIDとカテゴリIDが一致した場合、取り出し
    # json.loads()とjson()はどちらもjsonデータをpython形式に変更するが、json()はrequestsライブラリで使用されるメソッド
    # loads()は文字列を引数にとり、load()はファイルオブジェクト型を引数にとる
    # input_data:情報の詰まったリスト
    # フィルタされた施設一覧を返す
    # フィルタ結果リスト
    response = []
    input_data = json.loads(input_data)["data"]
    if filter_mode == "filter":
        if not input_filterIDs:
            response = input_data
        else:
            if filter_type == "or":
                for data in input_data:
                    # フィルタIDとカテゴリIDの数字部分が一致した場合、リストに追加
                    # リスト同士で一致する要素があるか確認
                    if set([filterID[1:] for filterID in input_filterIDs]) & set([category[1:] for category in data["category"]]):
                        response.append(data)
            elif filter_type == "and":
                for data in input_data:
                    # フィルタIDがカテゴリIDの部分集合だった場合、リストに追加
                    if set([filterID[1:] for filterID in input_filterIDs]) <= set([category[1:] for category in data["category"]]):
                        response.append(data)
    elif filter_mode == "search":
        if input_text != "":
            # オブジェクトをインスタンス化
            kakasi_instance = kakasi()
            # モードの設定
            # J(Kanji) to H(Hiragana)
            kakasi_instance.setMode("J", "K")
            # 変換器の用意
            convJtoK = kakasi_instance.getConverter()
            # K(Katakana) to a(ROMAN)
            kakasi_instance.setMode("K", "H")
            convKtoH = kakasi_instance.getConverter()
            # H(Hiragana) to a(ROMAN)
            kakasi_instance.setMode("H", "a")
            convHtoA = kakasi_instance.getConverter()
            for data in input_data:
                # アルファベットは小文字に変換
                if (convHtoA.do(convKtoH.do(convJtoK.do(data["name"]))).lower()).find(convHtoA.do(convKtoH.do(convJtoK.do(input_text))).lower()) != -1:
                    response.append(data)
    response = json.dumps({"data": response})
    return response