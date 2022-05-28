#Программа предназначена для унификации фотографий обуви с сайтов lamoda.ru и ... для формирования обучающей выборки
#Автор: Сафина А.М.
#На вход принимается каталог нужных изображений, класс и каталог для помещенаия туда унифицированных изображений
#Выходные данные: файлы формата jpeg, сохраняемые в заданную папку

from PIL import Image
import csv



def unification(path_to_unificate, gender, path_to_save):
    configuration = open('config.txt', 'r')
    text = configuration.readlines()
    amount = ''
    for i in text[26]:
        if i != "\n":
            amount = amount + i
        else:
            continue
    amount = int(amount)
    numb = 1
    go_name = 1
    while (numb <= amount): #укажите количество изображений

        image_file_name = path_to_unificate + '/' + str(numb) + '_' +  str(gender) + '_sketchers.jpeg'
        if(gender == "F"):
            filename = path_to_save + '/' + gender + '/' + str(go_name) + "_" + str(gender) +  "_" + "sketchers" + ".jpeg"
        if(gender == "M"):
            filename = path_to_save + '/' + gender + '/' + str(go_name) + "_" + str(gender) + "_" + "sketchers" + ".jpeg"
        im = Image.open(image_file_name).convert('RGB')
        im = im.crop((10,150,225,340))
        im.save(filename)
        numb = numb + 1
        go_name = go_name + 1

    return 0
