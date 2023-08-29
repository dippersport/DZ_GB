# DZ - 7
# Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. Поскольку разобраться в его 
# кричалках не настолько просто, насколько легко он их придумывает, Вам стоит написать программу. 
# Винни-Пух считает, что ритм есть, если число слогов (т.е. число гласных букв) в каждой фразе 
# стихотворения одинаковое. Фраза может состоять из одного слова, если во фразе несколько слов, 
# то они разделяются дефисами. Фразы отделяются друг от друга пробелами.


# def ritm(str):
#     str = str.split()
#     list = []
#     for num in str:
#         res = 0
#         for i in num:
#             if i in 'аеёиоуыэюя':
#                 res += 1
#         list.append(res)
#     return len(list) == list.count(list[0])


# Примеры тестов
# print(ritm("пара-ра-рам рам-пам-папам па-ра-па-дам"))  # True
# print(ritm("пара-ра-рам рам-пум-пупам па-ре-по-дам"))  # True
# print(ritm("пара-ра-рам рам-пуум-пупам па-ре-по-дам"))  # False
# print(ritm("Трам-пара-папам-парам-па-пам-пам-па Пум-пурум-пу-пурум-трам-пам-па"))  # False
# print(ritm("Пам-парам-пурум Пум-пурум-карам"))  # True


#DZ - 7.1
#  Напишите функцию print_operation_table(operation, num_rows=6, num_columns=6), которая принимает в 
# качестве аргумента функцию, вычисляющую элемент по номеру строки и столбца, т.е. функцию двух аргументов. 
# Аргументы num_rows и num_columns указывают число строк и столбцов таблицы, которые должны быть распечатаны. 
# Нумерация строк и столбцов идет с единицы.
# Примеры/Тесты:
# print_operation_table(lambda x,y: x**y,4,4)


# def print_operation_table(operation, num_rows=6, num_columns=6):
#     for row in range(1, num_rows + 1):
#         row_values = []
#         for column in range(1, num_columns + 1):
#             element = operation(row, column)
#             row_values.append(str(element))
#         print("\t".join(row_values))

# Пример использования
# def multiplication_operation(row, column):
#     return row * column

# print_operation_table(lambda x,y: x**y,4,4)