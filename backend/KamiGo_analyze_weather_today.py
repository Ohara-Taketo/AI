import datetime
import KamiGo_extraction_weather

# 今日の天気を解析
# 直接「KamiGo_extraction_weather.extraction_weather()」しないようにする必要あり。アクセス過多を防ぐ。
# 資料1:https://www.data.jma.go.jp/stats/data/mdrr/man/gaikyo.html
# 資料2:https://xml.kishou.go.jp/link.html
# 資料3:https://www.t3a.jp/blog/web-develop/weather-code-list/

# 天気コード分類
# 100:晴れ
sunny_100 = ["100", "101", "110", "111", "123", "124", "130", "131", "132"]
# 200:曇り
cloudy_200 = ["200", "201", "209", "210", "211", "223", "231"]
# 300:雨
sunny_300 = ["102", "103", "106", "107", "108", "112", "113", "114", "118", "119", "120", "121", "122", "125", "126", "127", "128", "140"]
cloudy_300 = ["202", "203", "206", "207", "208", "212", "213", "214", "218", "219", "220", "221", "222", "224", "225", "226", "240"]
rain_300 = ["300", "301", "302", "304", "306", "308", "311", "313", "316", "317", "320", "321", "323", "324", "325", "328", "329", "350"]
# 400:雪
sunny_400 = ["104", "105", "115", "116", "117", "160", "170", "181"]
cloudy_400 = ["204", "205", "215", "216", "217", "228", "229", "230", "250", "260", "270", "281"]
rain_400 = ["303", "309", "314", "315", "322", "326", "327", "340", "361", "371"]
snow_400 = ["400", "401", "402", "403", "405", "406", "407", "409", "411", "413", "414", "420", "421", "422", "423", "425", "426", "427", "450"]

def analyze_weather_today():
    # 情報取得
    (
    timeDefines_data1_3days,
    weatherCodes_areas_data1_3days,
    timeDefines_data2_3days,
    pops_areas_data2_3days,
    timeDefines_data1_7days,
    weatherCodes_areas_data1_7days,
    pops_areas_data1_7days,
    reliabilities_areas_data1_7days
    ) = KamiGo_extraction_weather.extraction_weather()
    #現在の時刻取得
    time_now = datetime.datetime.now()
    # 今日の日時作成
    date_today = time_now.strftime("%Y-%m-%d")
    # 今日の天気、降水確率取得
    for index_date, date in enumerate(timeDefines_data1_3days):
        if date.find(date_today) == 0:
            weather_code_today = weatherCodes_areas_data1_3days[index_date]
    # 現在の降水確率を取得
    for index_time, time in enumerate(timeDefines_data2_3days):
        if time.find(date_today) == 0:
            pop_now = int(pops_areas_data2_3days[index_time])
            break
    # 現在の天気を解析(絶対じゃないよ)
    if weather_code_today in sunny_100:
        weather_now = "晴れ"
    elif weather_code_today in sunny_300:
        if pop_now >= 80:
            weather_now = "高確率で雨"
        elif pop_now >= 50:
            weather_now = "雨かも"
        elif pop_now >= 20:
            weather_now = "晴れかも"
        else:
            weather_now = "晴れ"
    elif weather_code_today in cloudy_300:
        if pop_now >= 80:
            weather_now = "高確率で雨"
        elif pop_now >= 50:
            weather_now = "雨かも"
        elif pop_now >= 20:
            weather_now = "曇りかも"
        else:
            weather_now = "曇り"
    elif weather_code_today in rain_300:
        weather_now = "雨"
    print(weather_now)
analyze_weather_today()