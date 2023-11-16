import time


def func(list_a, list_b):
    set_list_b_using_id = {item["id"] for item in list_b}
    result = [dict_a.copy() for dict_a in list_a if dict_a["id"] in set_list_b_using_id]

    return result


data_a, data_b = [
    {"id": 1, "name": "John"},
    {"id": 2, "name": "Jane"},
    {"id": 1, "name": "John"},
    {"id": 3, "name": "Bob"},
    {"id": 2, "name": "Jane"},
] * 700, [
    {"id": 1, "name": "John"},
    {"id": 2, "name": "Jane"},
    {"id": 1, "name": "John"},
    {"id": 3, "name": "Bob"},
    {"id": 2, "name": "Jane"},
] * 1000
start_time = time.time()
func(data_a, data_b)
end_time = time.time()

print(f"Execution time: {end_time - start_time} seconds")
