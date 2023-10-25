from datetime import datetime

class MyStr(str):
    def __new__(cls, value, author):
        instance = super().__new__(cls, value)
        instance.author = author
        instance.value = value
        instance.time = datetime.now().strftime('%Y-%m-%d %H:%M')
        return instance

    def __str__(self):
        if self.author :
            return f'{str(self.value)} (Автор: {self.author}, Время создания: {self.time})'
        return f'{str(self.value)} (Автор: {self.author}, Время создания: [ в формате \'%Y-%m-%d %H:%M\'])'
                                                                     
    def __repr__(self):
        return f'MyStr({super().__repr__()}, {self.author!r})'
    

# Пример использования
event = MyStr("Завершилось тестирование", "John")
print(event)
#my_string = MyStr("Пример текста", "Иван")
#print(my_string)
my_string = MyStr("Мама мыла раму", "Маршак")
print(repr(my_string))

#Завершилось тестирование (Автор: John, Время создания: [ в формате '%Y-%m-%d %H:%M'])
#Пример текста (Автор: Иван, Время создания: 2023-10-10 15:56)
#MyStr('Мама мыла раму', 'Маршак')