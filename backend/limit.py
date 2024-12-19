import json

def limit(input_datas, limit_number):
    input_datas = json.loads(input_datas)["data"]
    response = input_datas[:limit_number]
    response = json.dumps({"data": response})
    return response