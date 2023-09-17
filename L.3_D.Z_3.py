
# 4. Программа загадывает число от 0 до 1000. Необходимо угадать число за 10 попыток. Программа
# должна подсказывать «больше» или «меньше» после каждой попытки. Для генерации случайного
# числа используйте код:
# from random import randint
# num = randint(LOWER_LIMIT, UPPER_LIMIT)

from random import randint

LOWER_LIMIT = 0
UPPER_LIMIT = 1000
SECRET = randint(LOWER_LIMIT, UPPER_LIMIT)
NUMBER = 10

print("Добро пожаловать в игру 'Угадай число'!")
print(f"Угадайте число от {LOWER_LIMIT} до {UPPER_LIMIT}. У вас есть {NUMBER} попыток.")

for num in range(1, NUMBER + 1):
    res = int(input(f"Попытка {num}: Введите число : "))
    
    if res < SECRET:
        print("Число больше.")
    elif res > SECRET:
        print("Число меньше.")
    else:
        print(f"Вы угадали число {SECRET} с {num} попытки.")
        break
else:
    print(f"Вы не угадали число. {SECRET}.")
