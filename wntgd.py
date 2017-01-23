import sys

from keras.datasets import mnist
from keras.models import Sequential
from keras.layers import Dense, Activation, normalization
from keras.layers.pooling import MaxPooling1D
from keras.layers.core import Flatten, Reshape
from keras.layers.recurrent import LSTM
from keras.layers.convolutional import ZeroPadding2D, Convolution2D
from keras.utils.np_utils import to_categorical
import numpy as np

print('Loading data')
(X_train, y_train), (X_test, y_test) = mnist.load_data()
print(X_train.shape)
seed = 7
np.random.seed(seed)



testsx = X_train
testsy = y_train




testsx = np.array(testsx)


model = Sequential()

model.add(LSTM(30, consume_less='gpu', input_shape = (28, 28)))
model.add(Dense(output_dim=20))
model.add(Dense(output_dim=20))
model.add(Dense(output_dim=10))
model.add(Dense(output_dim=1))
model.add(Activation("relu"))

#model.load_weights('Weights.hd5')

model.compile(
             loss='mean_absolute_error',
             optimizer='adam',
             )

history = model.fit(
    x=testsx,
    y=testsy,
    nb_epoch=50,
    verbose=1,
    validation_split=0.01,
    batch_size=64
)
print('-'*50)

model.save_weights('Weights.hd5')




