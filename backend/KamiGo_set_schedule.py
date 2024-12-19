from datetime import datetime

# 旅行の日程を設定する
def set_date():
    input_travel_start_date = input("旅行開始日を入力してください:")
    input_travel_end_date = input("旅行終了日を入力してください:")
    input_travel_start_date = datetime.strptime(input_travel_start_date, "%Y-%m-%d")
    input_travel_end_date = datetime.strptime(input_travel_end_date, "%Y-%m-%d")
    return (input_travel_start_date, input_travel_end_date)