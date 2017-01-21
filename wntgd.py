#! /usr/bin/env g
import sys
from keras.models import Sequential
from keras.layers import Dense, Activation, normalization
from keras.layers.pooling import MaxPooling1D
from keras.layers.core import Flatten, Reshape
from keras.layers.recurrent import LSTM
from keras.layers.convolutional import Convolution1D
from keras.utils.np_utils import to_categorical
import numpy as np

seed = 7
np.random.seed(seed)

sys.stdin = open('./conv.txt', 'r')

testsx = []
testsy = []

current = True
while True:
    try:
        inp = input()
    except EOFError:
        break
    if inp == "":
        break
    if current:
        #arr = np.zeros(10)
        #arr[int(inp)] = 1
        #testsy.append(arr)
        testsy.append((int(inp)+1)/10)
    else:
        arr = np.array(list(map(int,inp)))
        testsx.append(arr)
    current = not current

testsx = np.array(testsx)
testsy = np.array(testsy)

#testsy = to_categorical(testsy, nb_classes=None)

model = Sequential()
model.add(Reshape((32, 32),input_shape=(1024,)))

model.add(LSTM(100, consume_less='cpu'))


#model.add(Dense(output_dim=512))
#model.add(Activation("tanh"))
#model.add(Dense(output_dim=512))
#model.add(Activation("tanh"))
#model.add(Dense(output_dim=256))
#model.add(Activation("tanh"))
#model.add(Dense(output_dim=256))
#model.add(Activation("tanh"))
#model.add(Dense(output_dim=256))
#model.add(Activation("tanh"))
#model.add(Dense(output_dim=256))
#model.add(Activation("tanh"))

#model.add(Dense(output_dim=64))
#model.add(Activation("tanh"))
#model.add(Dense(output_dim=32))
#model.add(Activation("tanh"))

model.add(Dense(output_dim=1))
model.add(Activation("sigmoid"))

model.load_weights('Weights.hd5')

model.compile(
             loss='mean_absolute_error',
             optimizer='adam',
             #metrics=['accuracy']
             )

history = model.fit(
    x=testsx,
    y=testsy,
    nb_epoch=500,
    verbose=2,
    validation_split=0.1,
    batch_size=4
)
print('-'*50)

for i, elem in enumerate(model.predict(testsx)):
    print(elem, testsy[i])

model.save_weights('Weights.hd5')




