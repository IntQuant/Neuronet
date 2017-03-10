"""
 Реализация ИНС
"""
from keras.models import Sequential
from keras.layers import Dense, Activation, normalization, Dropout
from keras.layers.pooling import MaxPooling2D
from keras.layers.advanced_activations import PReLU
from keras.layers.convolutional import Convolution2D
from keras.layers.core import Reshape, Flatten
from keras.utils.visualize_util import plot
from keras.optimizers import SGD

import numpy as np

class GetModel:
	@staticmethod
	def getmodel():
		img_rows=28
		img_cols=28
		nb_classes=10
		
		print('Creating model')
		
		model = Sequential()
		
		# Два свёрточных слоя с максимумом по смежным
		
		model.add(Convolution2D(32, 3, 3, input_shape=(28, 28, 1)))
		model.add(Activation('relu'))
		model.add(MaxPooling2D(pool_size=(2, 2)))
		model.add(Convolution2D(32, 3, 3))
		model.add(Activation('relu'))
		model.add(MaxPooling2D(pool_size=(2, 2)))
		
		model.add(Flatten())  # Это превращает трёхмерные карты явлений
							  # в одномерные

	
		#Финальная обработка полностью связвнными слоями
	
		model.add(Dense(640))
		model.add(Activation('relu'))
		model.add(Dropout(0.5))
		model.add(Dense(320))
		model.add(Activation('relu'))
		model.add(Dropout(0.5))
		model.add(Dense(10))
		model.add(Activation('softmax'))
				
		plot(model, to_file='model.png')
		
		return model
		
