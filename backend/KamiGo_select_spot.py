import json
import KamiGo_extraction_weather

# 旅行プラン作成

input_prefecture_name = "kochi"
input_area_code = 390000
input_date = "2024-10-28" 
file_name = f"{input_prefecture_name}_sightseeing_spots.json"

# ファイルの内容を読み込む
with open(file_name, "r", encoding="utf-8") as f:
    list_data = json.load(f)  # loadならfだけ。loadsならf.read()。

# 時刻(天気)、地域、天気、時刻(降水確率)、降水確率
(
    timeDefines_weathers_3days,
    list_area_weathers_3days,
    list_code_weathers_3days,
    list_weather_weathers_3days,
    timeDefines_pops_3days,
    list_pop_pops_3days
) = KamiGo_extraction_weather.analyze_weather(input_area_code)

# 雨の天気コード
rain_codes = ["200", "300", "301", "302", "303", "304", "306", "307", "308", "309", "311", "313", "314", "315", "316", "317", "320", "321", "322", "323", "324", "325", "326", "327", "328", "329", "340", "350", "361", "371"]
sunny_sometimes_rain_codes = ["102", "103", "106", "107", "108"]
sunny_after_rain_codes = ["112", "113", "114", "118", "119"]

# 各観光地の現在のおすすめ度合いを計算
list_point = []
for index_time, time in enumerate(timeDefines_weathers_3days):
    if time.find(input_date) == 0:
        for index_area, area in enumerate(list_area_weathers_3days):
            for sightseeing_spot_data in list_data:
                if sightseeing_spot_data["area"].find(area) == 0:
                    # 雨かどうかを確認
                    if list_code_weathers_3days[index_area][index_time] in rain_codes:
                        if sightseeing_spot_data["spot_type"].find("屋外") == 0:
                            recommend_point = float(sightseeing_spot_data["point"]) * 0
                        elif sightseeing_spot_data["spot_type"].find("屋内外") == 0:
                            recommend_point = float(sightseeing_spot_data["point"]) * 0.5
                        else:
                            recommend_point = float(sightseeing_spot_data["point"])
                        point_json = {
                            "name": sightseeing_spot_data["name"],
                            "point": recommend_point
                            }
                        list_point.append(point_json)
    else:
        print(input_date + "の旅行プランは作成できません。")
print(list_point)



