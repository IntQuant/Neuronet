"""
 Neuronet implimentation
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
		
		filters = 64
		
		nb_conv = 3
		nb_pool = 2
		
		model = Sequential()
		
		model.add(Convolution2D(filters, nb_conv, nb_conv, border_mode='valid', input_shape=(img_rows, img_cols, 1)))
		model.add(Activation('relu'))
		model.add(Convolution2D(filters, nb_conv, nb_conv))
		model.add(Activation('relu'))
		model.add(MaxPooling2D(pool_size=(nb_pool, nb_pool)))
		model.add(Dropout(0.25))
		
		model.add(Flatten())	
		model.add(Dense(128))
		model.add(Activation('relu'))
		model.add(Dropout(0.5))

		model.add(Dense(nb_classes))
		model.add(Activation('softmax'))

		model.compile(loss='categorical_crossentropy',optimizer='adadelta',metrics=['accuracy'],								 
								 )
		
		plot(model, to_file='model.png')
		
		return model
		
