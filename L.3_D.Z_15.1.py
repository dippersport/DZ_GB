# На вход подается словарь со списком вещей для похода в качестве ключа и их массой max_weight в качестве значения.
# Определите какие вещи влезут в рюкзак backpack передав его максимальную грузоподъёмность.
# Результат должен быть в виде словаря с вещами в рюкзаке:{предмет:вес}
# *Верните все возможные варианты комплектации рюкзака.

# Задание

# Возьмите любые 1-3 задачи из прошлых домашних заданий.
# Добавьте к ним логирование ошибок и полезной
# информации. Также реализуйте возможность запуска из
# командной строки с передачей параметров.


# items = {
#     "ключи": 0.3,
#     "кошелек": 0.2,
#     "телефон": 0.5,
#     "зажигалка": 0.1
# }
# max_weight = 1.0

# from pprint import pprint

# backpacks = []

# for i in range(2**len(items)):
#     backpack = {}
#     weight = 0
#     for j, item in enumerate(items):
#         if i & (1 << j):
#             if weight + items[item] <= max_weight:
#                 backpack[item] = items[item]
#                 weight += items[item]
#             else:
#                 break
#     backpacks.append(backpack)

# result = [backpack for backpack in backpacks if backpack]

# pprint(result)


import argparse
import logging
from pprint import pprint

# Настройка логирования
logging.basicConfig(filename='backpacks.log', level=logging.INFO, encoding='UTF-8', filemode='w')

def generate_backpacks(items, max_weight):
    backpacks = []

    for i in range(2**len(items)):
        backpack = {}
        weight = 0
        for j, item in enumerate(items):
            if i & (1 << j):
                if weight + items[item] <= max_weight:
                    backpack[item] = items[item]
                    weight += items[item]
                else:
                    break
        backpacks.append(backpack)

    return [backpack for backpack in backpacks if backpack]

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Генерация рюкзаков с максимальным весом")
    parser.add_argument("--max_weight", type=float, default=1.0, help="Максимальный вес рюкзака")
    args = parser.parse_args()

    items = {
        "ключи": 0.3,
        "кошелек": 0.2,
        "телефон": 0.5,
        "зажигалка": 0.1
    }

    try:
        result = generate_backpacks(items, args.max_weight)
        pprint(result)
        logging.info("Результат:")
        for backpack in result:
            logging.info(backpack)
    except Exception as e:
        logging.error(f"Произошла ошибка: {e}")
