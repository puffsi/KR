# Программа предназначена для быстрой сборки фотографий одежды с сайта ozon.ru для формирования обучающей выборки
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

def ozon():
    return 0