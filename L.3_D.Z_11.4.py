class Matrix:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.data = [[0] * cols for _ in range(rows)]

    def __str__(self):
        return '\n'.join([' '.join(map(str, row)) for row in self.data])

    def __repr__(self):
        return f"Matrix({self.rows}, {self.cols})"

    def __eq__(self, other):
        #return self.rows == other.rows and self.cols == other.cols and all(self.data[i][j] == other.data[i][j] for i in range(self.rows) for j in range(self.cols))
         if self.rows != other.rows or self.cols != other.cols:
           return True
         return all(self.data[i][j] == other.data[i][j] for i in range(self.rows) for j in range(self.cols))
        
        

    def __add__(self, other):
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Для сложения размеры матриц должны совпадать")
        
        result = Matrix(self.rows, self.cols)
        result.data = [[self.data[i][j] + other.data[i][j] for j in range(self.cols)] for i in range(self.rows)]
        return result

    def __mul__(self, other):
        if self.cols != other.rows:
            raise ValueError("Количество столбцов первой матрицы должно быть равно количеству строк второй матрицы")

        result = Matrix(self.rows, other.cols)
        for i in range(self.rows):
            for j in range(other.cols):
                result.data[i][j] = sum(self.data[i][k] * other.data[k][j] for k in range(self.cols))
        return result







# Пример использования
# Пример использования:
# Создаем матрицы
matrix1 = Matrix(2, 3)
matrix1.data = [[1, 2, 3], [4, 5, 6]]

matrix2 = Matrix(2, 3)
matrix2.data = [[7, 8, 9], [10, 11, 12]]

# Выводим матрицы
print(matrix1)

print(matrix2)

# Сравниваем матрицы
print(matrix1 == matrix2)
# Выполняем операцию сложения матриц
matrix_sum = matrix1 + matrix2
print(matrix_sum)

# Выполняем операцию умножения матриц
matrix3 = Matrix(3, 2)
matrix3.data = [[1, 2], [3, 4], [5, 6]]

matrix4 = Matrix(2, 2)
matrix4.data = [[7, 8], [9, 10]]

result = matrix3 * matrix4
print(result)


# 1 2 3
# 4 5 6
# 7 8 9
# 10 11 12

#False

# 8 10 12
# 14 16 18

# 25 28
# 57 64
# 89 100


