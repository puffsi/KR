#Программа предназначена для унификации фотографий обуви с сайтов lamoda.ru и ... для формирования обучающей выборки
#Автор: Сафина А.М.
#На вход принимается каталог нужных изображений, класс и каталог для помещенаия туда унифицированных изображений
#Выходные данные: файлы формата jpeg, сохраняемые в заданную папку

from PIL import Image
import csv


# создание csv и txt файла
def unification():
    training_dir = input('Укажите, откуда брать фото:')
    gender = input('Укажите пол (F или M)')
    path = input("Укажите полный путь назначения для помещения туда фотографий: ")
    numb = 1
    go_name = 1
    f = open('filenames.txt', 'w')
    with open('markup_file.csv', 'w', newline='') as csvfile:
        while (numb <= 9641): #укажите количество изображений

            image_file_name = training_dir + '/' + str(numb) + '_' +  str(gender) + '_sketchers.jpeg'
            for_txt = str(go_name) + "_" + str(gender) +  "_" + "sketchers" + ".jpeg"
            filename = path + '/' + str(go_name) + "_" + str(gender) +  "_" + "sketchers" + ".jpeg"
            im = Image.open(image_file_name).convert('L')
            im = im.crop((10,150,225,340))
            filewriter = csv.writer(csvfile, delimiter=',',
                                    quotechar='|', quoting=csv.QUOTE_MINIMAL)
            filewriter.writerow([go_name, str(gender), 'sketchers'])
            f.write(for_txt + '\n')
            im.save(filename)
            numb = numb + 1
            go_name = go_name + 1
    f.close()
    print("Готово!")
    return 0

