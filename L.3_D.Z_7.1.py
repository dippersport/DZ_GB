# 1.Пример 
#Для начала нам нужно импортировать модуль NumPy как np.
import numpy as np

#создаем массив NumPy с именем arr_matrix.
arr_matrix = np.array([[1, 2, 3], [4, 5, 6]])

#вызываем метод transpose() для нашей матрицы – объекта arr_matrix
arr_transpose = arr_matrix.transpose()

# # выводим на экран исходную матрицу arr_matrix
print(arr_matrix)

#транспонированную матрицу arr_transpose,получили транспонированную матрицу
print(arr_transpose)

#[[1 4] 
# [2 5] 
#[3 6]]

# 2.Пример 
def transpose_matrix(matrix):
    # Определяем количество строк и столбцов в исходной матрице
    rows = len(matrix)
    cols = len(matrix[0])

    # Создаем новую пустую матрицу, меняя местами строки и столбцы
    transposed = [[0 for _ in range(rows)] for _ in range(cols)]

    # Заполняем новую матрицу значениями из исходной матрицы
    for i in range(rows):
        for j in range(cols):
            transposed[j][i] = matrix[i][j]

    return transposed
# Исходная матрица (3x2)
matrix = [
    [1, 2],
    [3, 4],
    [5, 6]
]

# Транспонируем матрицу
result = transpose_matrix(matrix)

# Выводим результат
for row in result:
    print(row)
