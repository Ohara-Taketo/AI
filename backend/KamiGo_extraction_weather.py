import json
from KamiGo_http import get_weather

# 天気を解析
# A:確度が高い、B:確度がやや高い、C:確度がやや低い
# 確度利用例:https://www.jma.go.jp/jma/kishou/know/kurashi/image/weekly_riyourei.pdf
# 命名規則:右が上位階層
# 命名ミスこわ

list_number_Kami_city = 0
list_number_Kochi_prefecture = 0
area_code = 390000


def extraction_weather():
    response = get_weather(area_code)
    # 3日間の情報
    Data_3days = response[0]
    # 観測所
    publishingOffice_3days = Data_3days["publishingOffice"]
    # 記録時刻
    reportDatetime_3days = Data_3days["reportDatetime"]
    # 3日間の情報
    timeSeries_3days = Data_3days["timeSeries"]
    # 天気をとる
    data1_3days = timeSeries_3days[0]
    # 時刻(リスト)
    timeDefines_data1_3days = data1_3days["timeDefines"]
    # エリア、天気コード、天気、風、波などが詰まったリスト
    areas_data1_3days = data1_3days["areas"]
    # 香美市は中部なのでリストの1つ目を回収
    Center_areas_data1_3days = areas_data1_3days[list_number_Kami_city]
    # 天気コード
    weatherCodes_areas_data1_3days = Center_areas_data1_3days["weatherCodes"]
    # 降水確率をとる
    data2_3days = timeSeries_3days[1]
    # 時刻(リスト)
    timeDefines_data2_3days = data2_3days["timeDefines"]
    # エリア、降水確率などが詰まったリスト
    areas_data2_3days = data2_3days["areas"]
    # 香美市は中部なのでリストの1つ目を回収
    Center_areas_data2_3days = areas_data2_3days[list_number_Kami_city]
    # 降水確率
    pops_areas_data2_3days = Center_areas_data2_3days["pops"]

    # 7日間の情報
    Data_7days = response[1]
    # 観測所
    publishingOffice_7days = Data_7days["publishingOffice"]
    # 記録時刻
    reportDatetime_7days = Data_7days["reportDatetime"]
    # 7日間の情報
    timeSeries_7days = Data_7days["timeSeries"]
    # 天気をとる
    data1_7days = timeSeries_7days[0]
    # 時刻(リスト)
    timeDefines_data1_7days = data1_7days["timeDefines"]
    # エリア、天気コード、降水確率、信頼度などが詰まったリスト
    areas_data1_7days = data1_7days["areas"]
    # リストの1つ目を回収
    Kochi_areas_data1_7days = areas_data1_7days[list_number_Kochi_prefecture]
    # 天気コード
    weatherCodes_areas_data1_7days = Kochi_areas_data1_7days["weatherCodes"]
    # 降水確率
    pops_areas_data1_7days = Kochi_areas_data1_7days["pops"]
    # 確度
    reliabilities_areas_data1_7days = Kochi_areas_data1_7days["reliabilities"]
    
    # 時刻(天気)、ウェザーコード、地域、天気、時刻(降水確率)、降水確率を返す
    return (
            timeDefines_data1_3days,
            weatherCodes_areas_data1_3days,
            timeDefines_data2_3days,
            pops_areas_data2_3days,
            timeDefines_data1_7days,
            weatherCodes_areas_data1_7days,
            pops_areas_data1_7days,
            reliabilities_areas_data1_7days
            )