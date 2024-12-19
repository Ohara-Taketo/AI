import json
import os

# inputはstr型で受け取る

# 施設名
spot_id = input("スポットID:")
# 施設名
name = input("施設名:")
# カテゴリID
category = list(iter(lambda: input("カテゴリ(「over」で終了):"), "over"))
# 識別
identification = input("識別:")


# jsonデータ作成
data_sightseeing_spot = {
    "spot_id": spot_id,
    "name": name,
    "category": category,
    "identification": identification
}

# ファイルの指定
file_name = f"Kami_spots.json"

# 既存のjsonファイルを読み込み、新しいデータを追加する
if os.path.exists(file_name):
    # ファイルが存在する場合、読み込む
    with open(file_name, "r", encoding = "utf-8") as f:
        try:
            # 既存のデータをロード
            data_list = json.load(f)
        except json.JSONDecodeError:
            # ファイルが空だった場合、新しいリストを作成
            data_list = []
else:
    # ファイルが存在しない場合、新しいリストを作成
    data_list = []

# 新しい観光地データをリストに追加
data_list.append(data_sightseeing_spot)

# jsonファイルに書き込む
with open(file_name, "w", encoding = "utf-8") as f:
    json.dump(data_list, f, ensure_ascii = False, indent = 4)
