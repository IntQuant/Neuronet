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
		
		
		
		
		
		
		model = Sequential()
		
		model.add(Convolution2D(32, 3, 3, input_shape=(28, 28, 1)))
		model.add(Activation('relu'))
		model.add(MaxPooling2D(pool_size=(2, 2)))
		model.add(Convolution2D(32, 3, 3))
		model.add(Activation('relu'))
		model.add(MaxPooling2D(pool_size=(2, 2)))
		
		model.add(Flatten())  # this converts our 3D feature maps to 1D feature vectors
		model.add(Dense(64))
		model.add(Activation('relu'))
		model.add(Dropout(0.5))
		model.add(Dense(64))
		model.add(Activation('relu'))
		model.add(Dropout(0.5))
		model.add(Dense(10))
		model.add(Activation('softmax'))

		model.compile(loss='categorical_crossentropy',optimizer='rmsprop',metrics=['accuracy'],								 
								 )
		
		plot(model, to_file='model.png')
		
		return model
		
