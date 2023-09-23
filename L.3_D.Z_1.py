
# 2.Треугольник существует только тогда, когда сумма любых двух его сторон больше третьей. 
# Дано a, b, c - стороны предполагаемого треугольника. Требуется сравнить длину каждого 
# отрезка-стороны с суммой двух других. Если хотя бы в одном случае отрезок окажется больше 
# суммы двух других, то треугольника с такими сторонами не существует. 
# Отдельно сообщить является ли треугольник разносторонним, равнобедренным или равносторонним.

def triangle(a, b, c):
    # Проверяем  треугольника
    if a + b > c and a + c > b and b + c > a:
        # Треугольник существует
        if a == b == c:
            return "Равносторонний треугольник"
        elif a == b or a == c or b == c:
            return "Равнобедренный треугольник"
        else:
            return "Разносторонний треугольник"
    else:
        return "Треугольник не существует"

# Задаем стороны треугольника
a = float(input("Введите длину стороны a: "))
b = float(input("Введите длину стороны b: "))
c = float(input("Введите длину стороны c: "))

# Проверяем и выводим результат
res = triangle(a, b, c)
print(res)