import requests
from bs4 import BeautifulSoup
import pandas as pd

# Чтение ID фильмов из файла
with open(r'C:\Users\home\Favorites\Documents\Downloads\id_kinopoisk.txt', 'r') as file:
    film_ids = [line.strip() for line in file]

# Создаем пустые списки для данных
ids = []
parts_of_movies = []
similar_movies_list = []

# Проходим по каждому ID фильма
for film_id in film_ids:
    url = f'https://www.kinopoisk.ru/film/{film_id}/'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Парсим части фильма
    parts = []
    parts_section = soup.find('a', {'name': 'parts'})
    if parts_section:
        parts = [part['href'].split('/')[2] for part in parts_section.find_all('a')]

    # Парсим похожие фильмы
    similar_movies = []
    similar_section = soup.find('div', {'class': 'block'})
    if similar_section:
        similar_links = similar_section.find_all('a', {'class': 'all'})
        if similar_links:
            similar_movies = [link['href'].split('/')[2] for link in similar_links]

    # Добавляем данные в соответствующие списки
    ids.append(film_id)
    parts_of_movies.append(', '.join(parts) if parts else None)
    similar_movies_list.append(', '.join(similar_movies) if similar_movies else None)

# Создаем DataFrame из списков
result_df = pd.DataFrame({'ID КиноПоиска': ids, 'Части фильма': parts_of_movies, 'Похожие фильмы': similar_movies_list})

# Сохраняем данные в текстовый файл
result_df.to_csv('kinopoisk_data.txt', index=False, sep='\t')

# Затем вы можете вручную конвертировать текстовый файл в Excel, если это необходимо.









