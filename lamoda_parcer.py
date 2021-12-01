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
def lamoda(link, path, how_much_pages):
    count = 0
    go_name = 0
    while count <= how_much_pages:
        pages = list(link)
        print(pages)
        pages[-1] = count
        link_1 = ''.join(str(v) for v in pages)
        print(link_1)
        url = urllib.request.urlopen(link_1)
        content = url.read()
        soup = BS(content)
        links = [a ['href'] for a in soup.find_all('a', href=re.compile('https.*\.jpg'))]
        links += [a ['href'] for a in soup.find_all('a', href=re.compile('https.*\.jpeg'))]
        imgs = [img ['src'] for img in soup.find_all('img', src=lambda x: x.endswith('.jpg'))]
        imgs += [img ['src'] for img in soup.find_all('img', src=lambda x: x.endswith('.jpeg'))]
        links += imgs
        new_links = []
        for a in links:
            a = "https:" + a
            new_links.append(a)

        print(len(new_links))
        print("\n".join(new_links))

        for link_1 in new_links:
            go_name = go_name + 1
            url = link_1
            filename = str(go_name) + ".jpeg"
            source_path = filename
            r = requests.get(url, allow_redirects=True)
            open(filename, 'wb').write(r.content)
            shutil.move(source_path, path)

        count = count + 1
    return 0

