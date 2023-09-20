#1.Напишите программу, которая получает целое число и возвращает его шестнадцатеричное строковое представление. 
#Функцию hex используйте для проверки своего результата.



def to_hex(n):
    if n < 0:
      return
    hex_chars = "0123456789ABCDEF"
    res = ""

    while n > 0:
        num = n % 16
        res = hex_chars[num] + res
        n = n // 16

    if res == "":
        res = "0"

    return res

# Пример использования
number = 255
hex_decimal = to_hex(number)
hex_string = hex(number)



# Проверяем, совпадают ли результаты
if hex_decimal == hex_string[2:].upper():  # Игнорируем "0x" и преобразуем в верхний регистр
    print("Результаты совпадают!")
else:
    print("Результаты не совпадают.")

