def get_file_info(file_path):
    file_name = file_path.split("/")[-1]
    file_extension = file_name.split(".")[-1]
    path = file_path[:-len(file_name)]
    return (path, file_name[:-len(file_extension)-1], "." + file_extension)




# Пример использования
file_path = "C:/Users/User/Documents/example.txt"
file_info = get_file_info(file_path)
print(file_info)
file_path = '/home/user/data/file' 
file_info = get_file_info(file_path)
print(file_info)
file_path = 'D:/myfile.txt'
file_info = get_file_info(file_path)
print(file_info)
file_path = 'C:/Projects/project1/code/script.py'
file_info = get_file_info(file_path)
print(file_info)
file_path = '/home/user/docs/my.file.with.dots.txt'
file_info = get_file_info(file_path)
print(file_info)

#1('C:/Users/User/Documents/', 'example', '.txt')
#2file_path = '/home/user/data/file'      
#2'/home/user/data/', '', '.file')

#3file_path = 'D:/myfile.txt'
#3('D:/', 'myfile', '.txt')

#4file_path = 'C:/Projects/project1/code/script.py'
#4('C:/Projects/project1/code/', 'script', '.py')

#5file_path = '/home/user/docs/my.file.with.dots.txt'
#5('/home/user/docs/', 'my.file.with.dots', '.txt')

#6file_path = 'file_in_current_directory.txt'


