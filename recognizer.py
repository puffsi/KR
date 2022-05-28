from tensorflow.keras.models import load_model
import cv2
classes = ['Женская', 'Мужская']

def recognize(model_path, test_path, start_pic_m, start_pic_f, until_m, until_f, protocol_name):
    model = load_model(model_path)
    model.summary()
    amount_male = int(until_m)
    male_start = int(start_pic_m)
    amount_female = int(until_f)
    female_start = int(start_pic_f)
    FJ = 0
    TM = 0
    TJ = 0
    FM = 0

    def prepare(filepath):
        img_height = 215
        img_width = 190
        img_array = cv2.imread(filepath, cv2.IMREAD_COLOR)
        new_array = cv2.resize(img_array, (img_height, img_width))
        return new_array.reshape(1,img_height, img_width,3)

    while(male_start <= amount_male):

        img_now = test_path + "/" + str(male_start) + '_M_sketchers.jpeg'
        prediction = model.predict([prepare(img_now)])
        print(str(classes [int(prediction[0][0])]))
        if (str(classes[int(prediction[0][0])]) == "Мужская"):
            TM += 1
            male_start += 1
        else:
            FJ += 1
            male_start += 1

    while (female_start<=amount_female):
        img_now = test_path + "/" + str(female_start) + '_F_sketchers.jpeg'
        prediction = model.predict([prepare(img_now)])
        if (str(classes [int(prediction[0][0])]) == "Женская"):
            TJ += 1
            female_start += 1
        else:
            FM += 1
            female_start += 1
    

    f = open(protocol_name, 'w')
    accuracy = (TJ + TM)/(amount_male+amount_female)
    precision = TJ/(TJ+FJ)
    recall = TJ/(TJ+FM)
    fscore = (2*precision*recall)/(precision+recall)
    f.write("Accuracy: " + str(accuracy))
    f.write("\nPrecision: " +  str(precision))
    f.write(" \nRecall: " + str(recall))
    f.write( "\nF-score: " + str(fscore) + '\n')
    f.write("\nConfusion matrix: \n\n\n")
    f.write("                         PREDICTED FEMALE     " + "PREDICTED MALE")
    f.write("\nACTUAL FEMALE                   " + str(TJ) + "                " + str(FM) + '\n')
    f.write("\nACTUAL MALE                     " + str(FJ) + "                " + str(TM))
    f.close()
