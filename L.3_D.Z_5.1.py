#2.Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем.
#Программа должна возвращать сумму и произведение* дробей. 
#Для проверки своего кода используйте модуль fractions.

from fractions import Fraction

def parse_fraction(str):
     # Разбиваем строку дроби и преобразуем числитель и знаменатель в int
     num, den = map(int, str.split('/'))
     return num, den

def calculate_sum_product(str1, str2):
    # Рассчитываем сумму и произведение дробей
    sum_num = str1[0] * str2[1] + str2[0] * str1[1]
    product_num = str1[0] * str2[0]
    product = str1[1] * str2[1]
    return sum_num, product_num, product

fraction_str1 = "2/3"
fraction_str2 = "1/4"

str1 = parse_fraction(fraction_str1)
str2 = parse_fraction(fraction_str2)

sum_num, product_num, product = calculate_sum_product(str1, str2)

# Печать результатов
print("Сумма дробей:", f"{sum_num}/{str1[1] * str2[1]}")
print("Произведение дробей:", f"{product_num}/{product}")



fraction1 = Fraction(fraction_str1)
fraction2 = Fraction(fraction_str2)

# Сумма дробей с использованием fractions
sum_fraction = fraction1 + fraction2

# Произведение дробей с использованием fractions
product_fraction = fraction1 * fraction2

# Печать результатов
print("Сумма дробей (fractions):", sum_fraction)
print("Произведение дробей (fractions):", product_fraction)

# Сравнение с вашими рассчитанными значениями
print("Сравнение с рассчитанными значениями:")
print("Сумма дробей (ваш код):", f"{sum_num}/{str1[1] * str2[1]}")
print("Произведение дробей (ваш код):", f"{product_num}/{product}")

