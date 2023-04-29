import cv2
from pprint import pprint
from termcolor import cprint
import bs4
import peewee
import requests

# Шаг 1 - выкачиваем картинки с https://course.skillbox.ru/profession-python

# html = requests.get('https://sheer82.ru/kontakty/').text
# html = requests.get('https://prodoctorov.ru/moskva/dietolog/').text
# html = requests.get('https://uristus.ru/our-team-of-lawyers/').text
html = requests.get('https://realstudy.ru/nashi-prepodavateli.html').text


soup = bs4.BeautifulSoup(html, 'html.parser')
all_img = soup.find_all('img')
# pprint(all_img)
# print('\n'.join(str(t.get('data-original', t.get('src'))) for t in all_img if 'Mask_Group' in str(t)))
# print('\n'.join(str(t.get('data-original', t.get('src'))) for t in all_img))

downloaded_files = []
for tag in all_img:
    url = tag.get('data-original', tag.get('src'))
    if url:
        filename = url.split('/')[-1]
        if len(filename.split('.')[-1]) == 3:
            filename = f'./photos/{filename}'
            if url.split('/')[0] != 'https:':
                url = 'https://realstudy.ru' + url
            downloaded_files.append(filename)
            print('Добавлен в список картинок адрес:', url)
            try:
                with open(filename, mode='wb') as ff:
                    ff.write(requests.get(url).content)
            except:
                cprint(f'Ошибка записи файла - {filename}', color='red')
                continue
# pprint(downloaded_files)

#
for img_path in downloaded_files:
    face_cascade = cv2.CascadeClassifier('external_data/haarcascade_frontalface_default.xml')
    image = cv2.imread(img_path)
    try:
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    except Exception as err:
        # cprint(f'{err} for {image}', color='red')
        continue
    faces = face_cascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(10, 10)
    )
    if len(faces):
        cprint(f'Есть лицо - {img_path}', color='green')
