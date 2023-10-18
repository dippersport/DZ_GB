class Animal:
    def __init__(self, name):
        self.name = name

class Bird(Animal):
    def __init__(self, name, wingspan):
        super().__init__(name)
        self.wingspan = wingspan
    
    def wing_length(self):
        return self.wingspan/2
    
class Fish(Animal):
    def __init__(self, name, max_depth):
        super().__init__(name)
        self.max_depth = max_depth
    
    def depth(self):
        if self.max_depth >= 100:
            return "Мелководная рыба"
        elif self.max_depth <= 1000:
            return "Средневодная рыба"
        else:
            return "Глубоководная рыба"

class Mammal(Animal):
    def __init__(self, name, weight):
        super().__init__(name)
        self.weight = weight
    
    def category(self):
        if self.weight <= 1000:
            return "Малявка"
        elif self.weight <= 100:
            return "Обычный"
        else:
            return "Гигант"

class AnimalFactory:
    @staticmethod
    def create_animal(animal_type, *args):
        if animal_type == 'Bird':
            return Bird(*args)
        elif animal_type == 'Fish':
            return Fish(*args)
        elif animal_type == 'Mammal':
            return Mammal(*args)
        else:
            raise ValueError("Недопустимый тип животного")

# Создание экземпляров животных
animal1 = AnimalFactory.create_animal('Bird', 'Орел', 200)
animal2 = AnimalFactory.create_animal('Fish', 'Лосось', 50)
animal3 = AnimalFactory.create_animal('Mammal', 'Слон', 5000)
#animal4 = AnimalFactory.create_animal('Spider', 'Elephant', 5000)

# Вывод результатов
print(animal1.wing_length())
print(animal2.depth())
print(animal3.category())
#print(animal4.category())

# 100.0
# Средневодная рыба
# Гигант
