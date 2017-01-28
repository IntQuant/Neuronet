import sys

from keras.datasets import mnist
from keras.models import Sequential
from keras.layers import Dense, Activation, normalization, Dropout
from keras.layers.pooling import MaxPooling1D
from keras.layers.core import Flatten, Reshape
from keras.layers.recurrent import LSTM
from keras.layers.convolutional import MaxPooling1D, Convolution1D
from keras.utils.np_utils import to_categorical
from keras.optimizers import SGD
import numpy as np

print('Loading data')
(X_train, y_train), (X_test, y_test) = mnist.load_data()
print(X_test.shape)
seed = 7
np.random.seed(seed)

model = Sequential()
model.add(LSTM(150, consume_less='gpu', input_shape = (28, 28)))
model.add(Dense(output_dim=50))
model.add(Activation("relu"))
model.add(Dense(output_dim=1))
model.add(Activation("relu"))
print('Loading weights')
model.load_weights('Weights.hd5')
print('Predicting')
predicted = model.predict(X_test)
print('Calculating perfomance')
perfomance = [0]*10
numcount = [0]*10
totalperc = 0
for answer, predicted in zip(y_test, predicted):
	if int(float(predicted)+0.5) == int(answer):
		perfomance[answer] += 1
	numcount[answer] += 1

for i, predansw in enumerate(zip(perfomance, numcount)):
	pred = predansw[0]
	answ = predansw[1]
	perc = int((pred/answ)*1000)/10
	totalperc += perc
	print(str(i)+' -->',
	      perfomance[i],
	      'of',
	      numcount[i],
	      perc,'%',
	      sep='\t'
	      )
print('Total:',totalperc/10,'%')
