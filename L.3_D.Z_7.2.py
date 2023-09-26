#1. Пример
def create_dict(**kwargs):
    result_dict = {}
    for key, value in kwargs.items():
        if isinstance(key, (int, float, str, bool)):
            key_name = key
        else:
            key_name = str(key)
        result_dict[key] = key_name
    return result_dict

# Пример использования
args_dict = create_dict(a=1, b='example', c=[1, 2, 3])
print(args_dict)

#2.Пример
def create_dict(*args):
    result_dict = {}
    for i, value in enumerate(args):
        if isinstance(value, (int, float, str, bool)):
            key = value
        else:
            key = str(value)
        result_dict[key] = i
    return result_dict

# Пример использования
args_dict = create_dict(1, 'example', [1, 2, 3])
print(args_dict)




