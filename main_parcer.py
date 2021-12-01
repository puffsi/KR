#Программа предназначена для быстрой сборки фотографий одежды с сайтов lamoda.ru и ... для формирования обучающей выборки
#Автор: Сафина А.М.
#На вход принимается ссылка на страницу, содержащую каталог нужной одежды, путь к папке, куда помещаются фото, а также
#необходимое кол-во страниц для обработки
#Выходные данные: в модулях


from bs4 import BeautifulSoup as BS
import urllib.request
from lamoda_parcer import lamoda
def main_parcer():
    all_links = ['https://www.lamoda.ru/c/2968/shoes-krossovki-kedy/?page=1', 'https://www.lamoda.ru/c/2981/shoes-krossovk-kedy-muzhskie/?page=1']
    all_pages = [167, 161]

    link = input("Какой каталог спарсить? Введите число(ссылки находятся в текстовом файле):")
    if int(link) == 1:
        link = all_links[0]
        my_page = all_pages[0]
    elif int(link) == 2:
        link = all_links[1]
        my_page = all_pages[1]
    else:
        return 0

    path = input("Укажите полный путь назначения для помещения туда фотографий: ")
    how_much_pages = int(input("Укажите, сколько страниц спарсить " + "(максимум " + str(my_page) + "): "))
    print("Работает парсер для сайта lamoda... ")
    lamoda(link, path, how_much_pages)
    print("Готово!")
    return 0

main_parcer()