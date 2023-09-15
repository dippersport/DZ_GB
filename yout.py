from pytube import YouTube

# URL видео на YouTube
#video_url = "https://youtu.be/ZlfKYEG-eXk"
video_url1 = "https://youtu.be/Qe-2Cv5zd84"
# Создаем объект YouTube
yt = YouTube(video_url1)

# Выбираем первый поток (с наивысшим качеством)
video_stream = yt.streams.get_highest_resolution()

# Скачиваем видео в текущую директорию
video_stream.download()

print("Видео скачано успешно!")
