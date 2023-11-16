import time


def find_duplicates(input_list):
    sorted_list = sorted(input_list, key=lambda x: (x["id"], x["name"]))

    duplicates = []

    for i in range(1, len(sorted_list)):
        if sorted_list[i] == sorted_list[i - 1]:
            duplicates.append(sorted_list[i])

    return duplicates


data = [
    {"id": 1, "name": "John"},
    {"id": 2, "name": "Jane"},
    {"id": 1, "name": "John"},
    {"id": 3, "name": "Bob"},
    {"id": 2, "name": "Jane"},
] * 2000

start_time = time.time()
result = find_duplicates(data)
end_time = time.time()

print(f"Execution time: {end_time - start_time} seconds")
