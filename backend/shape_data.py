def shape_data(list, data, data_type):
    # 返り値を使わなくてもlist(response)は更新される
    list.append({
    f"{data_type}_id": data[f"{data_type}_id"],
    "name": data["name"],
    "identification": data["identification"]
    })