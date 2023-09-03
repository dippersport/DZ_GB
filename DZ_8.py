
import os

def get_user_data() -> list:
    name = input('Введите имя:  ')
    sur_name = input('Введите фамилию: ')
    phone_num = input('Введите номер телефона: ')
    desc = input('Введите описание: ')
    lastname = input('Введите первую часть фамилии для выбора: ')

    return [name, sur_name, phone_num, desc, lastname]
def create_record(gb_phone_book: list, user_data: list) -> list:
    gb_phone_book.append(user_data)
    return gb_phone_book

def delete_record(gb_phone_book: list, sur_name: str) -> list:
    updated_phone_book = [record for record in gb_phone_book if record[1] != sur_name]
    return updated_phone_book

def select_lastname(gb_phone_book: list, lastname: str) -> list:
    selected_records = []
    for record in gb_phone_book:
        if record[1].startswith(lastname):
            selected_records.append(record)
    
            selected_records.append(record)
    return selected_records

def print_phone_book(gb_phone_book:list) -> None:
    for record in gb_phone_book:
        print(record)

def get_file_name() -> str:
    return input('Введите имя файла: ')

def create_from_data(gb_phone_book: list, file_name:str,delimiter:str) -> list:
    path_sourse= os.path.join('.', file_name)
    with open(path_sourse,'r', encoding='utf-8') as sourse:
        for line in sourse:
            gb_phone_book = create_record(gb_phone_book, line.strip().split(delimiter))
    return gb_phone_book


def menu():
    phone_book = list()
    while True:
        print('Введите 1 для выхода из справочника')
        print('Введите 2 для создание новой записи')
        print('Введите 3 для вывода на экран ')
        print('Введите 4 для импорта данных из файла')
        print('Введите 5 для выбора записей по фамилии')
        print('Введите 6 для удаления записи по фамилии')

        choise = int(input('Ваш выбор: '))
        if choise == 1:
            print('Вы выбрали выход')
            return
        if choise == 2:
            phone_book = create_record(phone_book, get_user_data())

        if choise == 3:
            print_phone_book(phone_book)
        if choise == 4:
            phone_book= create_from_data(phone_book, get_file_name(),',')
        if choise == 5:
            lastname = input('Введите первую часть фамилии для поиска: ')
            selected_records = select_lastname(phone_book, lastname)
            print('Найденные записи:')
            print_phone_book(selected_records)
        if choise == 6:
            sur_name_to_delete = input('Введите фамилию для удаления записи: ')
            phone_book = delete_record(phone_book, sur_name_to_delete)
            
            phone_book = delete_record
            print('Запись удалена.')


menu()