#Программа предназначена для подготовки обучающей базы, используя изображения с сайтов lamoda.ru и ...
#для формирования обучающей выборки
#Автор: Сафина А.М.
#На вход принимается число, соответствующее операции, которую нужно провести
#Выходные данные: файлы формата jpeg, сохраняемые в заданную папку

from main_parcer import main_parcer
from unificator import unification
def preprocessor():
    choice = int(input(("Выберите нужную операцию:\n 1. Парсинг\n 2. Унификация\n")))
    if choice == 1:
        print("Запускаю парсинг...")
        main_parcer()
    if choice == 2:
        print("Запускаю унификацию...")
        unification()
    else:
        print("Нет такой операции!")

    return 0
preprocessor()