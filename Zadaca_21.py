# 4.1[22]: Даны два неупорядоченных набора целых чисел (может быть, с повторениями). Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах. Если таких чисел нет - выдать внятное диагностическое сообщение
# Наборы (списки) чисел можно считать заданными и не вводить с клавиатуры

# Примеры/Тесты:
# Input1: 2 4 6 8 10 12 10 8 6 4 2
# Input2: 3 6 9 12 15 18
# Output: 6 12     Обратите внимание: Без скобочек, в одну строку

# Input1: 2 4 6 8 10 10 8 6 4 2
# Input2: 3 9 12 15 18
# Output: Повторяющихся чисел нет



n_1 = [2, 4, 6, 8, 10, 12, 10, 8, 6, 4, 2]
m_1 = [3, 6, 9, 12, 15, 18]
a_1 = set(sorted(n_1))
b_1 = set(sorted(m_1))
print(*sorted(a_1 & b_1))

n_2 = [2, 4, 6, 8, 10, 10, 8, 6, 4, 2]
m_2 = [3, 9, 12, 15, 18]
a_2 = set(sorted(n_2))
b_2 = set(sorted(m_2))
print(*sorted(a_2&b_2))
print('Повторяющихся чисел нет')



