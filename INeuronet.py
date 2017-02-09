"""
 Neuronet implimentation
"""
from keras.models import Sequential
from keras.layers import Dense, Activation, normalization, Dropout
from keras.layers.pooling import MaxPooling2D
from keras.layers.advanced_activations import PReLU
from keras.layers.core import Reshape
import numpy as np

class GetModel:
	@staticmethod
	def getmodel():
		model = Sequential()
		model.add(Dense(32, input_shape=(1, 32 ,32)))
		model.add(Activation('sigmoid'))
		model.add(MaxPooling2D())
		model.add(Dense(32))
		model.add(Activation('sigmoid'))
		model.add(MaxPooling2D())
		model.add(Dense(32))
		model.add(Activation('sigmoid'))
		model.add(MaxPooling2D())
		model.add(Dense(32))
		model.add(Activation('sigmoid'))
		model.add(MaxPooling2D())
		model.add(Reshape((2, 16)))
		model.add(Dense(1))
		model.add(Activation('softmax'))
		
		return model
		
