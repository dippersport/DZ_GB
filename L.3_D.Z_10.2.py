class LotteryGame:
    def __init__(self, list1, list2):
        self.list1 = list1
        self.list2 = list2

    def compare_lists(self):
        matching_numbers = []  # Инициализируем список для совпадающих чисел

        for num1 in self.list1:
            if num1 in self.list2:
                matching_numbers.append(num1)
        if matching_numbers:
            print("Совпадающие числа:", matching_numbers)
            print("Количество совпадающих чисел:", len(matching_numbers))
        else:
            print("Совпадающих чисел нет.")

        return matching_numbers



#list1 = [3, 12, 8, 41, 7, 21, 9, 14, 5, 30]  # Ваш лотерейный билет
#list2 = [9, 5, 6, 12, 14, 22, 17, 41, 8, 3]  # Выпавшие числа
#game = LotteryGame(list1, list2)
#matching_numbers = game.compare_lists()
    
list1 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
list2 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
game = LotteryGame(list1, list2)
matching_numbers = game.compare_lists()

#list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#list2 = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
#game = LotteryGame(list1, list2)
#matching_numbers = game.compare_lists()

#Совпадающие числа: [3, 12, 8, 41, 9, 14, 5]
#Количество совпадающих чисел: 7

#Совпадающие числа: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
#Количество совпадающих чисел: 10

#Совпадающих чисел нет.

