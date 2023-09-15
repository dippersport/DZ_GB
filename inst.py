import requests
import wget
from pytube import YouTube

img_url = 'https://media.istockphoto.com/id/1470234996/photo/woman-sitting-in-a-fitness-studio-with-her-yoga-class.jpg?s=1024x1024&w=is&k=20&c=zOimJ22xpyUnsfd6eZgGNYM7NW6PoMoh2AAEk5Ouhks='

video_url = 'https://youtu.be/qdfLQ5_4g_o?t=2'

img2_url = 'https://www.instagram.com/p/Cw5w4oPvfIs/?next=%2F'

video2_url = 'https://www.instagram.com/p/CwD5rmYIokk/?next=%2F'
def dowloand_img(url=''):

    try:
        response = requests.get(url=url)

        with open('req_img.jpg', 'wb') as file:
            file.write(response.content)

        return 'Img successfully downloaded!'
    
    except Exception as  _ex:
        return 'Upps... Check the URL please!'

def dowloand_video(url=''):

    try:
        #response = requests.get(url=url)

        #with open('req_video.mp4', 'wb') as file:
            #file.write(response.content)

        response = requests.get(url=url, stream=True)

        with open('req_video.mp4', 'wb') as file:
            for chunk in response.iter_content(chunk_size=1024 * 1024):
                if chunk:
                    file.write(chunk)

        return 'Video successfully downloaded!'
    
    except Exception as _ex:
        return 'Upps... Check the URL please!'
    
def dowloand_wget(url='', file_type='video'):
    try:
        if file_type == 'video':
            wget.download(url=url, out=f'wget_{file_type}.mp4')
        else:
            wget.download(url=url, out=f'wget_i{file_type}.jpg')

    except Exception as _ex:
        return 'Upps... Check the URL please!'

def main():
    print(dowloand_img(url=img_url))
    print(dowloand_video(url=video_url))
    dowloand_wget(url=img2_url)
    dowloand_wget(url=video2_url)
if __name__ == '__main__':
    main()





    #pip install -r requirements.txt     pip freeze > requirements.txt
