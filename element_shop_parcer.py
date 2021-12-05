# Программа предназначена для быстрой сборки фотографий одежды с сайта https://elementshop.ru для формирования обучающей выборки
# Автор: Сафина А.М.
# На вход принимается ссылка на страницу, содержащую каталог нужной одежды, путь к папке, куда помещаются фото, а также
# необходимое кол-во страниц для обработки
# Выходные данные: файлы формата jpeg, сохраняемые в заданную папку
import img as img
import requests
from bs4 import BeautifulSoup as BS
import urllib.request
import re
import shutil
from os import path

def element_shop():
    link = "https://elementshop.ru/catalog/shoes/-vid-krossovki/pol-muzh/"
    pages = list(link)
    print(pages)
    count = pages[-1]
    link_1 = ''.join(str(v) for v in pages)
    print(link_1)
    r = requests.get(link_1)
    html = BS(r.content, 'html.parser')
    imgs = [img ['src'] for img in html.find_all('img', src=lambda x: x.endswith('.png.webp'))]
    print(imgs)
    print(len(imgs))
    return 0

    '''
            for link_1 in new_links:
                if (choice == 1):
                        gender = 'F'
                else:
                    gender = "M"
                go_name = go_name + 1
                url = link_1
                filename = str(go_name) + "_" + gender + "_" + "sketchers" + ".jpeg"
                source_path = filename
                r = requests.get(url, allow_redirects=True)
                open(filename, 'wb').write(r.content)
                shutil.move(source_path, path)
    
            count = count + 1
            '''
