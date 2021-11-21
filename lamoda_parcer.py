#Программа предназначена для быстрой сборки фотографий одежды с сайта lamoda.ru для формирования обучающей выборки
#Автор: Сафина А.М.
#На вход принимается ссылка на страницу, содержащую каталог нужной одежды, путь к папке, куда помещаются фото, а также
#необходимое кол-во страниц для обработки
#Выходные данные: файлы формата jpeg, сохраняемые в заданную папку

import requests
from bs4 import BeautifulSoup as BS
import urllib.request
import re
import shutil
from os import path

link = input("Введите ссылку на каталог (сайт): ")
path = input("Укажите полный путь назначения для помещения туда фотографий: ")
#how_much_pages = int(input("Укажите, сколько страниц спарсить: "))
#count = 1
#while count <= how_much_pages:
    #pages = list(link)
    #print(pages)
    #pages[-2] = count
    #link = str(pages)
url = urllib.request.urlopen(link)
content = url.read()
soup = BS(content)
links = [a ['href'] for a in soup.find_all('a', href=re.compile('https.*\.jpg'))]
imgs = [img ['src'] for img in soup.find_all('img', src=lambda x: x.endswith('.jpg'))]
new_links = []
links += imgs
new_links = []
for a in links:
    a = "https:" + a
    new_links.append(a)

print(len(new_links))
print("\n".join(new_links))

for link in new_links:
    url = link
    filename = url.split('/') [-1]
    source_path = filename
    r = requests.get(url, allow_redirects=True)
    open(filename, 'wb').write(r.content)
    shutil.move(source_path, path)

# count = count + 1
