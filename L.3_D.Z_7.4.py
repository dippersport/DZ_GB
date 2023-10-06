# ✔ Напишите функцию группового переименования файлов. Она должна:
# ✔ принимать параметр желаемое конечное имя файлов.
# При переименовании в конце имени добавляется порядковый номер.
# ✔ принимать параметр количество цифр в порядковом номере.
# ✔ принимать параметр расширение исходного файла.
# Переименование должно работать только для этих файлов внутри каталога.
# ✔ принимать параметр расширение конечного файла.
# ✔ принимать диапазон сохраняемого оригинального имени. Например для диапазона
# [3, 6] берутся буквы с 3 по 6 из исходного имени файла. К ним прибавляется
# желаемое конечное имя, если оно передано. Далее счётчик файлов и расширение

import os

def rename_files(directory, desired_name, num_digits, original_extension, final_extension, name_range):
    
    # Получаем список файлов в указанной директории с указанным расширением
    files = [f for f in os.listdir(directory) if f.endswith(original_extension)]
    
    # Переменная для отслеживания порядкового номера
    counter = 1
    
    # Проходимся по каждому файлу и переименовываем его
    for file_name in files:
        # Получаем полный путь к файлу
        file_path = os.path.join(directory, file_name)
        
        # Извлекаем имя файла без расширения и разделяем его на части
        file_name_without_extension, file_ext = os.path.splitext(file_name)
        
        # Если указан диапазон сохраняемого оригинального имени, обрезаем его
        if name_range:
            file_name_without_extension = file_name_without_extension[name_range[0]-1:name_range[1]]
        
        # Создаем новое имя файла с указанным конечным расширением и желаемым именем
        new_file_name = f"{file_name_without_extension}_{desired_name}_{counter:0{num_digits}d}.{final_extension}"
        
        # Создаем новый полный путь к файлу с новым именем
        new_file_path = os.path.join(directory, new_file_name)
        
        # Переименовываем файл
        os.rename(file_path, new_file_path)
        
        # Увеличиваем счетчик
        counter += 1
    print("Файлы успешно переименованы.")
   

# Пример использования
directory = r'C:\Users\home\Desktop\Lesson_3'  # Путь к директории с файлами
desired_name = "newname"  # Желаемое конечное имя файлов
num_digits = 3  # Количество цифр в порядковом номере
original_extension = ".jpg"  # Расширение исходных файлов
final_extension = "png"  # Расширение конечных файлов
name_range = (3, 6)  # Диапазон букв в оригинальном имени (например, с 3 по 6)

rename_files(directory, desired_name, num_digits, original_extension, final_extension, name_range)
