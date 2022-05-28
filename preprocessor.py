#Программа предназначена для подготовки обучающей базы, используя изображения с сайтов lamoda.ru и ...
#для формирования обучающей выборки
#Автор: Сафина А.М.
#На вход принимается число, соответствующее операции, которую нужно провести
#Выходные данные: файлы формата jpeg, сохраняемые в заданную папку

from parcer import lamoda
from unificator import unification
configuration = open('config.txt', 'r')
text = configuration.readlines()

def preprocessing(use):
    path = ""
    path_to_unificate = ''
    path_to_save = ''
    if (use == 'parcer'):
        gender = text[9][0]
        for i in text[11]:
            if i != "\n":
                path = path + i
            else:
                continue
        HowManyPages = int(text[13])
        if(gender == 'F'):
            link = 'https://www.lamoda.ru/c/2968/shoes-krossovki-kedy/?page=1'
            print("Запускаю парсинг...")
            lamoda(link, path, HowManyPages, gender)
            print("Готово!")
        if(gender == 'M'):
            link = 'https://www.lamoda.ru/c/2981/shoes-krossovk-kedy-muzhskie/?page=1'
            print("Запускаю парсинг...")
            lamoda(link, path, HowManyPages, gender)
            print("Готово!")
    if (use == 'unificator'):
        for i in text[20]:
            if i != "\n":
                path_to_unificate =  path_to_unificate + i
            else:
                continue
        gender = text[22][0]
        for i in text[24]:
            if i != "\n":
                path_to_save =  path_to_save + i
            else:
                continue
        print("Запускаю унификацию...")
        unification(path_to_unificate, gender, path_to_save)
        print("Готово!")
    else:
        print("Нет такой операции!")

    return 0
