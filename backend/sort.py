import json

def sort(input_datas, sort_key):
    input_datas = json.loads(input_datas)["data"]
    # キー「f"{sort_key}_point"」を基にソート
    if not input_datas:
        response = input_datas
    else:
        response = sorted(input_datas, key = lambda x: x[f"{sort_key}_point"], reverse = True)
    response = json.dumps({"data": response})
    return response