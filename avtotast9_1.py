





# import csv
# import json
# import random

# def save_to_json(func):
#     def wrapper(*args):
#         result_list = []
#         with open(args[0], 'r') as f:
#             reader = csv.reader(f)
#             for row in reader:
#                 a, b, c = map(int, row)
#                 result = func(a, b, c)
#                 data = {'parameters': [a, b, c], 'result': result}
#                 result_list.append(data)
#         with open('results.json', 'w') as f:
#             json.dump(result_list, f)
#     return wrapper

# @save_to_json
# def find_roots(a, b, c):
#     d = b ** 2 - 4 * a * c
#     if d < 0:
#         return None
#     elif d == 0:
#         return -b / (2 * a)
#     else:
#         x1 = (-b + d ** 0.5) / (2 * a)
#         x2 = (-b - d ** 0.5) / (2 * a)
#         return x1, x2

# def generate_csv_file(file_name, rows):
#     with open(file_name, 'w', newline='') as f:
#         writer = csv.writer(f)
#         for i in range(rows):
#             row = [random.randint(1, 1000) for _ in range(3)]
#             writer.writerow(row)
# # bu yoxlamag ucundu
# generate_csv_file("input_data.csv", 101)
# find_roots("input_data.csv")

# with open("results.json", 'r') as f:
#     data = json.load(f)

# if 100<=len(data)<=1000:
#     print(True)
# else:
#     print(f"Количество строк в файле не находится в диапазоне от 100 до 1000.")

# print(len(data)==101)

# 2. Создайте файл __init__.py и запишите в него все функции:
# save_to_json,
# find_roots,
# generate_csv_file.

code_to_write = '''

import os
import json
import csv
import pickle
import random

def generate_csv_file(file_name, rows):
    with open(file_name, 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(['a', 'b', 'c'])

        for _ in range(rows):
            a, b, c = random.randint(1, 100), random.randint(1, 100), random.randint(1, 100)
            csv_writer.writerow([a, b, c])

def find_roots(a, b, c):
    discriminant = b ** 2 - 4 * a * c
    if discriminant > 0:
        x1 = (-b + discriminant ** 0.5) / (2 * a)
        x2 = (-b - discriminant ** 0.5) / (2 * a)
        return x1, x2
    elif discriminant == 0:
        x = -b / (2 * a)
        return x
    else:
        return None

def save_to_json(func):
    def wrapper(file_name):
        results = []
        if not os.path.exists(file_name):
            print(f"Файл {file_name} не найден.")
            return

        with open(file_name, 'r') as csvfile:
            csv_reader = csv.reader(csvfile)
            next(csv_reader)  # Пропускаем заголовок
            for row in csv_reader:
                a, b, c = int(row[0]), int(row[1]), int(row[2])
                roots = find_roots(a, b, c)
                if roots is not None:
                    result = {'a': a, 'b': b, 'c': c, 'roots': roots}
                    results.append(result)

        with open('results.json', 'w') as jsonfile:
            json.dump(results, jsonfile, indent=2)

    return wrapper '''

            


with open("__init__.py", "w") as init_file:
    init_file.write(code_to_write)
















