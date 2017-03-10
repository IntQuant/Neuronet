""" Программа для обучения ИНС """

import sys

import numpy as np
import random
from INeuronet import GetModel
from PrepImg import Prepare
from keras.optimizers import SGD
from keras.callbacks import ReduceLROnPlateau, CSVLogger, TensorBoard
from keras.preprocessing.image import ImageDataGenerator as datagenc

seed = 7
np.random.seed(seed)
random.seed(seed)

#Получение модели. Сама модель находится в файле
# INeuronet.py
model = GetModel.getmodel()
currentbath = 0

#Получение датасета
testsx, testsy , xtest, ytest= Prepare.get()

rlr = ReduceLROnPlateau(monitor='val_loss', factor=0.2,
                  patience=2, min_lr=1e-7)
csvlog = CSVLogger('training.csv', append=True)
tb = TensorBoard()

callb = [rlr, csvlog, tb]



#Генератор изображений
datagen = datagenc( 
 rotation_range = 30,
 zoom_range = [0.9, 1.2],
 width_shift_range=0.2,
 height_shift_range=0.2, 
)



gen = datagen.flow(testsx, testsy, batch_size = 128)

model.compile(loss='categorical_crossentropy',optimizer='rmsprop')

history = model.fit_generator(
     generator = gen,
     samples_per_epoch = 12800,
     nb_epoch=20,
     verbose=1,
     validation_data = (xtest, ytest),
     callbacks = callb
 )
 
#Делаем первый слой не тренеруемым: это позволяет сделать fine-tuning 
model.layers[0].trainable = False

#Используем замедленный оптимизатор
csgd = SGD(lr=1e-4, momentum=0.9)

model.compile(loss='categorical_crossentropy',optimizer=csgd)

history = model.fit_generator(
     generator = gen,
     samples_per_epoch = 12800,
     validation_data = (xtest, ytest),
     nb_epoch=60,
     initial_epoch=20,
     verbose=1,
     callbacks = callb
 )



 
print(model.predict(testsx[0].reshape(1, 28, 28, 1)))

model.save_weights('Weights.hd5')

ev = model.evaluate(testsx, testsy)

print('Score:', ev[0])
print('Acc:  ', ev[1])



