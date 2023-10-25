# Введите ваше решение ниже

from typing import Union
class Archive:
    """
    Класс, представляющий архив текстовых и числовых записей.

    Атрибуты:
    - archive_text (list): список архивированных текстовых записей.
    - archive_number (list): список архивированных числовых записей.
    - text (str): текущая текстовая запись для добавления в архив.
    - number (int или float): текущая числовая запись для добавления в архив.
    """

    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.archive_text = []
            cls._instance.archive_number = []
        else:
            cls._instance.archive_text.append(cls._instance.text)
            cls._instance.archive_number.append(cls._instance.number)
        return cls._instance

    def __init__(self, text: str, number: Union[int, float]):
        self.text = text
        self.number = number

    def __str__(self):
        return f'Text is {self.text} and number is {self.number}. Also {self.archive_text} and {self.archive_number}'

    def __repr__(self):
        return f'Archive("{self.text}", {self.number})'












# archive1 = Archive("First Text", 1)
# print(archive1)

# archive2 = Archive("Second Text", 2)
# print(archive2)

# archive3 = Archive("Third Text", 3)
# print(archive1)
# print(archive3)




# Text is First Text and number is 1. Also [] and []
# Text is Second Text and number is 2. Also ['First Text'] and [1]
# Text is Third Text and number is 3. Also ['First Text', 'Second Text'] and [1, 2]
# Text is Third Text and number is 3. Also ['First Text', 'Second Text'] and [1, 2]

archive1 = Archive("First Text", 1)
archive2 = Archive("Second Text", 2)
archive3 = Archive("Third Text", 3)
print(archive1.archive_text)  # Выведет: ['First Text', 'Third Text']
print(archive1.archive_number)  # Выведет: [1, 3]
print(archive2.archive_text)  # Выведет: ['First Text', 'Second Text']
print(archive2.archive_number)
# ['First Text', 'Second Text']
# [1, 2]
# ['First Text', 'Second Text']
# [1, 2]