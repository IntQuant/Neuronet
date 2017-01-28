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
print(X_train.shape)
seed = 7
np.random.seed(seed)





testsx = X_train
testsy = y_train




testsx = np.array(testsx)


model = Sequential()
model.add(LSTM(150, consume_less='gpu', input_shape = (28, 28)))
model.add(Dense(output_dim=50))
model.add(Activation("relu"))
model.add(Dense(output_dim=1))
model.add(Activation("relu"))

model.load_weights('Weights.hd5')

fstartEpoch = int(input('Start epoch: '))
fstageepoch = int(input('fstageepoch: ')) + fstartEpoch
sstartEpoch = fstageepoch
sstageepoch = int(input('sstageepoch: ')) + sstartEpoch

model.compile(
             loss='mean_squared_error',
             optimizer='RMSprop',
             )

history = model.fit(
    x=testsx,
    y=testsy,
    nb_epoch=fstageepoch,
    initial_epoch=fstartEpoch,
    verbose=1,
    validation_split=0.01,
    batch_size=10
)

model.save_weights('Weights2.hd5')

for layer in model.layers[1:3]:
    layer.trainable = False
print('-'*50)

csgd = SGD(lr=1e-4, momentum=0.9)

model.compile(
             loss='mean_absolute_error',
             optimizer=csgd,
             )


history = model.fit(	
    x=testsx,
    y=testsy,
    nb_epoch=sstageepoch,
    initial_epoch=sstartEpoch,
    verbose=1,
    validation_split=0.01,
    batch_size=8
)



model.save_weights('Weights.hd5')




