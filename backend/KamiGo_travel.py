import json
from KamiGo_fil import filter
from KamiGo_select_mainspot import select_mainspot
from KamiGo_search import search
from KamiGo_set_schedule import set_date
from datetime import datetime

# 仮置き
file_name = "Kami_spots.json"
# ファイルの内容を読み込む
with open(file_name, "r", encoding = "utf-8") as f:
    # 辞書型にする
    list_spots = json.load(f)  # loadならfだけ。loadsならf.read()。
    # json文字列に戻す
    list_spots = json.dumps(list_spots)

# ちょいと整形
dify_list_spots = filter(list_spots, ["f001", "f002", "f003", "f004", "f005", "f006"])


# list_spotsはランキング順に観光地データが入っていることが望ましい

# 「検索」、「条件で探す」、「工科大生のイチオシ!」、「プランを作成」で条件分岐
# IDの先頭識別子によりどのアクションが選択されたか判断(fならフィルタなど)
# S:検索、f:条件で探す、s:工科大生のイチオシ!、b001:プランを作成
list_filed_spots = json.dumps([])
travel_start_date = ""
travel_end_date = ""
print(json.loads(list_spots))
while True:
    T001_input_action = input("T001_アクション:")
    if T001_input_action == "S":
        input_text = input("検索:")
        if input_text != "":
            # 検索結果を返す
            list_searched_spots = search(list_spots, input_text)
            # リストが空かどうか判定
            if not json.loads(list_searched_spots):
                print("ヒットなし")
            else:
                print(f"{json.loads(list_searched_spots)}がヒットしました")
            while True:
                T00x_input_action = input("T00x_アクション:")
                if T00x_input_action == "S":
                    input_text = input("検索:")
                    if input_text != "":
                        # 検索結果を返す
                        list_searched_spots = search(list_spots, input_text)
                        if not json.loads(list_searched_spots):
                            print("ヒットなし")
                        else:
                            print(f"{json.loads(list_searched_spots)}がヒットしました")
                elif T00x_input_action[0] == "s":
                    # メインスポットを設定する
                    main_spot = select_mainspot(list_searched_spots, T00x_input_action)
                    print(f"メインスポットは{json.loads(main_spot)["name"]}です")
                    break
                elif T00x_input_action == "b001":
                    # 「プラン作成画面」に移る
                    break
                elif T00x_input_action == "b002":
                    # 旅行日程を設定する
                    (travel_start_date, travel_end_date) = set_date()
                    print(f"旅行開始日は{travel_start_date}、旅行終了日は{travel_end_date}です")
            break
    elif T001_input_action[0] == "f":
        # フィルタ結果を返す
        list_filed_spots = filter(list_spots, [T001_input_action])
        print(f"フィルタ結果:{json.loads(list_filed_spots)}")
        while True:
            T002_input_action = list(iter(lambda: input("T002_アクション(「exit」で終了):"), "exit"))
            if all(input[0] == "f" for input in T002_input_action):
                # フィルタ結果を返す
                list_filed_spots = filter(list_spots, T002_input_action)
                print(f"フィルタ結果:{json.loads(list_filed_spots)}")
            elif T002_input_action[0][0] == "s":
                    # メインスポットを設定する
                    main_spot = select_mainspot(list_filed_spots, T002_input_action[0])
                    print(f"メインスポットは{json.loads(main_spot)["name"]}です")
                    break
            elif T002_input_action[0] == "b001":
                # 「プラン作成画面」に移る
                break
            elif T002_input_action[0] == "b002":
                # 旅行日程を設定する
                (travel_start_date, travel_end_date) = set_date()
                print(f"旅行開始日は{travel_start_date}、旅行終了日は{travel_end_date}です")
        break
    elif T001_input_action[0] == "s":
        # メインスポットを設定する
        main_spot = select_mainspot(list_spots, T001_input_action)
        print(f"メインスポットは{json.loads(main_spot)["name"]}です")
        break
    elif T001_input_action == "b001":
        # 「プラン作成画面」に移る
        break



# 「プラン作成画面」
# ここまででフィルタされていたらdifyのナレッジをlist_filted_spotsで更新、フィルタされていなかったらlist_spotsで更新
while True:
    T003_input_action = list(iter(lambda: input("T003_アクション(「exit」で終了):"), "exit"))
    if all(input[0] == "f" for input in T003_input_action):
        # メインスポット以外の観光地をフィルタ結果から決める?
        # フィルタ結果を返す
        list_filed_spots = filter(list_spots, T003_input_action)
        print(f"フィルタ結果:{json.loads(list_filed_spots)}")
    elif T003_input_action[0][0] == "s":
        # メインスポットを設定する
        main_spot = select_mainspot(list_spots, T003_input_action[0])
        print(f"メインスポットは{json.loads(main_spot)["name"]}です")
    elif T003_input_action[0] == "b002":
        # 旅行日程を設定する
        (travel_start_date, travel_end_date) = set_date()
        print(f"旅行開始日は{travel_start_date}、旅行終了日は{travel_end_date}です")
    elif T003_input_action[0] == "b003":
        # difyのナレッジ更新に移る
        break


# difyのナレッジを更新するリスト
if not json.loads(list_filed_spots):
    list_update_dify = json.loads(dify_list_spots)
else:
    list_update_dify = json.loads(list_filed_spots)

# メインスポットをリストが含んでいるか確認
if not json.loads(main_spot) in list_update_dify:
    list_update_dify.append(json.loads(main_spot))

# 日程を設定できるか確認
if travel_start_date != ""  and travel_end_date != "":
    difference = travel_end_date - travel_start_date
    travel_schedule = f"{difference.days - 1}泊{difference.days}日"
else:
    travel_schedule = "日帰り"

print(list_update_dify)
print(travel_schedule)


