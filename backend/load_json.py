import json

# テスト用
# ファイルの内容を読み込む
def load_json():
    with open("Kami_spots.json", "r", encoding = "utf-8") as f:
        # 辞書型にする
        list_spots = json.load(f)  # loadならfだけ。loadsならf.read()。
        # json文字列に戻す
        list_spots = json.dumps(list_spots)
    return list_spots