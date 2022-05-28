#Программа предназначена для реализации работы по обучению нейронной сети: от создания обучающей выборки до тестирования
#Автор: Сафина А.М.
#На вход принимается конфигурационный файл
#Выходные данные: в зависимости от параметров в конфигурационном файле
from preprocessor import preprocessing
from neural_network_1 import neural_network_1
from recognizer import recognize

configuration = open('config.txt', 'r')
text = configuration.readlines()
if (str(text[2][0:10]) == "Use? - yes"):
    if (str(text[6][0:10]) == "Use? - yes"):
        use_parcer = "parcer"
        preprocessing(use_parcer)
    if (str(text[17][0:10]) == 'Use? - yes'):
        use_unificator = "unificator"
        preprocessing(use_unificator)

if(str(text[30][0:10]) == "Use? - yes"):
    train_dir = ''
    where_to_save = ''
    for i in text [33]:
        if i != "\n":
            train_dir = train_dir + i
        else:
            continue
    for i in text [35]:
        if i != "\n":
            where_to_save = where_to_save + i
        else:
            continue
    neural_network_1(train_dir, where_to_save)
if(str(text[43][0:10]) == "Use? - yes"):
    model_path = ''
    test_path = ''
    start_pic_m = ''
    start_pic_f = ''
    until_m = ''
    until_f = ''
    protocol_name = ''
    for i in text [46]:
        if i != "\n":
            model_path = model_path + i
        else:
            continue
    for i in text [48]:
        if i != "\n":
            test_path = test_path + i
        else:
            continue
    for i in text [50]:
        if i != "\n":
            start_pic_m = start_pic_m + i
        else:
            continue
    for i in text [52]:
        if i != "\n":
            start_pic_f = start_pic_f + i
        else:
            continue
    for i in text [54]:
        if i != "\n":
            until_m = until_m + i
        else:
            continue
    for i in text [56]:
        if i != "\n":
            until_f = until_f + i
        else:
            continue
    for i in text [58]:
        if i != "\n":
            protocol_name = protocol_name + i
        else:
            continue
    recognize(model_path, test_path, start_pic_m, start_pic_f, until_m, until_f, protocol_name)