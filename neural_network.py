#Программа предназначена для создания нейронной сети и ее обучения
#Автор: Сафина А.М.
#На вход ничего не принимается
#Выходные данные: сигнал о завершении процесса обучения

from tensorflow.python.keras.preprocessing.image import ImageDataGenerator
from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D
from keras.layers import Activation, Dropout, Flatten, Dense

train_dir = 'C:/Users/Алина/Desktop/КР/unificated/train'
test_dir= 'C:/Users/Алина/Desktop/КР/unificated/test'

datagen = ImageDataGenerator(rescale=1. / 255)
img_width, img_height = 215, 190
input_shape = (img_width, img_height, 3)
epochs = 40
batch_size = 20
train_samples = 17608
test_samples = 2017

model = Sequential()
model.add(Conv2D(32, (3, 3), input_shape=input_shape))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))

model.add(Conv2D(32, (3, 3)))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))

model.add(Conv2D(64, (3, 3)))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))

model.add(Flatten())
model.add(Dense(64))
model.add(Activation('relu'))
model.add(Dropout(0.5))
model.add(Dense(1))
model.add(Activation('sigmoid'))

model.compile(loss='binary_crossentropy',
              optimizer ='adam',
              metrics=['accuracy'])

train_generator = datagen.flow_from_directory(
    train_dir,
    target_size=(img_width, img_height),
    batch_size=batch_size,
    class_mode='binary')
test_generator = datagen.flow_from_directory(
    test_dir,
    target_size=(img_width, img_height),
    batch_size=batch_size,
    class_mode='binary')

model.fit_generator(
    train_generator,
    steps_per_epoch=train_samples//batch_size,
    epochs=epochs
)