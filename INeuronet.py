"""
 Реализация ИНС
"""
from keras.models import Model
from keras.layers import Dense, Activation, normalization, Dropout, Input
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
		
		
		
		# Два свёрточных слоя с максимумом по смежным
		
		inp = Input((28, 28, 1))
		
		p = Convolution2D(32, 3, 3, activation='relu')(inp)
		p = MaxPooling2D(pool_size=(2, 2))(p)
		p = Convolution2D(32, 3, 3, activation='relu')(p)
		p = MaxPooling2D(pool_size=(2, 2))(p)
		
		p = Flatten()(p)  # Это превращает трёхмерные карты явлений
							  # в одномерные

	
		#Финальная обработка полностью связанными слоями
	
		p = Dense(640, activation='relu')(p)
		p = Dropout(0.5)(p)
		p = Dense(320, activation='relu')(p)
		data = Dropout(0.5)(p)
		classes = Dense(10, activation='softmax', name='classif')(data)
		isclassified = Dense(1, activation='sigmoid', name='isclass')(data)
		
		model = Model(input=inp, output=[classes, isclassified])
		
		
		
		plot(model, to_file='model.png')
		
		return model
		
