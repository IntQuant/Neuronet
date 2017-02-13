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

import numpy as np

class GetModel:
	@staticmethod
	def getmodel():
		img_rows=32
		img_cols=32
		nb_classes=10
		
		nb_conv = 2
		nb_pool = 2
		
		model = Sequential()
		
		model.add(Convolution2D(32, nb_conv, nb_conv, border_mode='valid', input_shape=(4, img_rows, img_cols)))
		model.add(Activation('relu'))
		model.add(Convolution2D(32, nb_conv, nb_conv))
		model.add(Activation('relu'))
		model.add(MaxPooling2D(pool_size=(nb_pool, nb_pool)))
		model.add(Dropout(0.25))

		model.add(Flatten())
		model.add(Dense(32*32))
		model.add(Activation('relu'))
		model.add(Dropout(0.5))
	
		model.add(Dense(256))
		model.add(Activation('relu'))
		model.add(Dropout(0.5))

		model.add(Dense(nb_classes))
		model.add(Activation('sigmoid'))

		model.compile(loss='categorical_crossentropy', optimizer='adadelta')
		
		plot(model, to_file='model.png')
		
		return model
		
