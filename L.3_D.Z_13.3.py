class InvalidNameError(Exception):
    pass

class InvalidAgeError(Exception):
    pass

class InvalidIdError(Exception):
    pass

class Person:
    def __init__(self, last_name, first_name, middle_name, age):
        if not isinstance(last_name, str) or not last_name.strip():
            raise InvalidNameError(f"Invalid name: . Name should be a non-empty string.")
        if not isinstance(first_name, str) or not first_name.strip():
            raise InvalidNameError(f"Invalid name: first name should be a non-empty string.")
        if not isinstance(middle_name, str) or not middle_name.strip():
            raise InvalidNameError(f"Invalid name: middle name should be a non-empty string.")
        if not isinstance(age, int) or age <= 0:
            raise InvalidAgeError(f"Invalid age: {age}. Age should be a positive integer.")
        
        self.last_name = last_name
        self.first_name = first_name
        self.middle_name = middle_name
        self.age = age

    def birthday(self):
        self.age += 1

    def get_age(self):
        return self.age

class Employee(Person):
    def __init__(self, last_name, first_name, middle_name, age, id):
        super().__init__(last_name, first_name, middle_name, age)
        
        if not isinstance(id, int) or not (100000 <= id <= 999999):
            raise InvalidIdError(f"Invalid id: {id}. Id should be a 6-digit positive integer between 100000 and 999999.")
        
        self.id = id

    def get_level(self):
        return sum(int(digit) for digit in str(self.id)) % 7





# Примеры использования:

#person = Person("", "John", "Doe", 30)
#print(person)

#Ожидаемый ответ:
#__main__.InvalidNameError: Invalid name: . Name should be a non-empty string.
#Ваш ответ:
#__main__.InvalidNameError: Invalid last name

person = Person("Alice", "Smith", "Johnson", -5)
print()

# Ожидаемый ответ:
# __main__.InvalidAgeError: Invalid age: -5. Age should be a positive integer.
# Ваш ответ:
# __main__.InvalidAgeError: Invalid age

#employee = Employee("Bob", "Johnson", "Brown", 40, 12345)
#print()


# Ожидаемый ответ:
# __main__.InvalidIdError: Invalid id: 12345. Id should be a 6-digit positive integer between 100000 and 999999.
# Ваш ответ:
# __main__.InvalidIdError: Invalid ID

# person = Person("Alice", "Smith", "Johnson", 25)
# print(person.get_age())

# Ожидаемый ответ:
# 25
# Ошибка:
# Traceback (most recent call last):
#   File "HIL2DNGWRL7RL7IS7HQJ.py", line 60, in <module>
#     print(person.get_age())
# AttributeError: 'Person' object has no attribute 'get_age'