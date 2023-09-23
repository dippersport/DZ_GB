import re
from collections import Counter

def top_10_words(text):
    words = re.findall(r'\b\w+\b', text.lower())
    return Counter(words).most_common(10)
#text = 'Hello world. Hello Python. Hello again.'
#text = 'This is a sample text without repeating words'
#text = "Python 3.9 is the latest version of Python. It's awesome!"
#text = 'Python is python, is, IS, and PYTHON.'

#print(top_10_words(text))
#[('hello', 3), ('world', 1), ('python', 1), ('again', 1)]
#[('this', 1), ('is', 1), ('a', 1), ('sample', 1), ('text', 1), ('without', 1), ('repeating', 1), ('words', 1)]
#[('python', 2), ('is', 1), ('the', 1), ('latest', 1), ('version', 1), ('of', 1), ('it', 1), ('s', 1), ('awesome', 1)]


import re
from collections import Counter

#text = "Python 3.9 is the latest version of Python. It's awesome!"
#text = 'Hello world. Hello Python. Hello again.'
#text = 'This is a sample text without repeating words'
#text = "Python 3.9 is the latest version of Python. It's awesome!"
text = 'Python is python, is, IS, and PYTHON.'

# Используем регулярное выражение для выделения слов, не содержащих цифр
words = re.findall(r'\b[^\d\W]+\b', text.lower())

# Подсчитываем количество вхождений каждого слова
word_counts = Counter(words)

# Получаем 10 самых частых слов
most_common_words = word_counts.most_common(10)

print(most_common_words)

