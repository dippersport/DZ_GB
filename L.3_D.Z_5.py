#2.Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем.
#Программа должна возвращать сумму и произведение* дробей. 
#Для проверки своего кода используйте модуль fractions.

from fractions import Fraction

def cal_fractions(example):
    # Разбиваем входную строку на числитель и знаменатель
    nums = example.split('/')
    
    if len(nums) != 2:
        return 
    
    end = int(nums[0])
    res = int(nums[1])
    
    # Создаем объекты Fraction для дробей
    fraction = Fraction(end, res)
    
    # Вычисляем сумму и произведение
    total_sum = fraction
    product = 1  # Начальное значение для произведения
    
    # Чтобы вычислить произведение, мы умножаем числитель и знаменатель каждой дроби
    for num in nums:
        number = int(num)
        product *= number
    
    return f"Сумма: {total_sum}, Произведение: {product}"

# Пример использования
input_str = "2/5"
result = cal_fractions(input_str)
print(result)
