import json
INPUT_FILE = "input.csv"


def csv_to_list_dict(filename, delimiter=',') -> list[dict]:
    list_row = []
    list_dict = []
    with open("input.csv", "r") as f:
        rows = f.readlines()
        headers_data = rows[0].rstrip().split(sep=",")
        for row in rows[1:]:
            list_row.append(rows.rstrip().split(sep=","))

        for element in list_row:
            list_dict = dict(zip(headers_data, element))
            list_dict.append(dict)

    return list_dict


print(json.dumps(csv_to_list_dict(INPUT_FILE), indent=4))
