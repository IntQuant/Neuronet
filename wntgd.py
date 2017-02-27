""" Программа для обучения ИНС """

import sys

import numpy as np
import random
from INeuronet import GetModel
from PrepImg import Prepare
from keras.optimizers import SGD
from keras.preprocessing.image import ImageDataGenerator as datagenc

seed = 7
np.random.seed(seed)
random.seed(seed)

#Получение модели. Сама модель находится в файле
# INeuronet.py
model = GetModel.getmodel()
currentbath = 0

#Получение датасета
testsx, testsy = Prepare.get()


#Генератор изображений
datagen = datagenc( 
 rotation_range = 30,
 zoom_range = [0.9, 1.2],
 width_shift_range=0.2,
 height_shift_range=0.2, 
)


def dataprep():
	global datagen
	global testsx
	global testsy
	gen = datagen.flow(testsx, testsy, batch_size = 128)
	
	while True:
		bit = random.getrandbits(1) == 1
		#bit = False
		if bit:
			#print('Using generator')
			(testx, testy) = next(gen)
			
			inp = {'input_1':testx}
			out = {'classif':testy, 'isclass':np.array([1]*128)}
			if out['classif'].shape == (128, 10):
				yield (inp, out)
			
		else:
			#print('Creating stm random')
			rand = np.random.random((128, 28, 28, 1))
			class_out = np.array([[0]*10]*128)
			
			inp = {'input_1':rand}
			out = {'classif':class_out, 'isclass':np.array([0]*128)}
			yield (inp, out)

sh1 = sh2 = [128, 28, 28, 1]





model.compile(loss=['categorical_crossentropy', 'binary_crossentropy'],optimizer='rmsprop', loss_weights=[1., 0.2])

print(len(model.input_names),model.internal_input_shapes)
print(model.output_names)

history = model.fit_generator(
     generator = dataprep(),
     samples_per_epoch = 12800,
     nb_epoch=10,
     verbose=1,
 )
 
#Делаем первый слой не тренеруемым: это позволяет сделать fine-tuning 
model.layers[0].trainable = False

#Используем замедленный оптимизатор
csgd = SGD(lr=1e-4, momentum=0.9)

model.compile(loss=['categorical_crossentropy', 'binary_crossentropy'],optimizer=csgd , loss_weights=[1., 0.5])

history = model.fit_generator(
     generator = dataprep(),
     samples_per_epoch = 12800,
     nb_epoch=17,
     verbose=1,
 )



 
print(model.predict(testsx[0].reshape(1, 28, 28, 1)))

model.save_weights('Weights.hd5')

ev = model.evaluate(testsx, testsy)

print('Score:', ev[0])
print('Acc:  ', ev[1])



