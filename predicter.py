import argparse
import sys
import math



from keras.models import Sequential
from keras.layers import Dense, Activation, normalization
from keras.layers.pooling import MaxPooling1D
from keras.layers.core import Flatten, Reshape
from keras.layers.recurrent import LSTM
from keras.layers.convolutional import Convolution1D
from keras.utils.np_utils import to_categorical
import numpy as np

#from sklearn import preprocessing
from skimage import io, transform
from skimage.color import rgb2gray

parser = argparse.ArgumentParser(description='Neuronet for reading numbers from images')
parser.add_argument('Path', type=str, help='Path to predict from')

args = parser.parse_args()

model = Sequential()
model.add(Flatten(input_shape = (28, 28)))
model.add(Dense(output_dim=28*4))
model.add(Activation("sigmoid"))
model.add(Dense(output_dim=1))
model.add(Activation("relu"))

model.load_weights('Weights/Weights-auto491.hd5')

io.use_plugin('matplotlib')

udata = io.imread(args.Path) #as_grey=True)

udata = transform.resize(udata, output_shape=(28, 28, 4))

data = np.empty((28, 28), dtype = np.uint8)
for i in range(28):
	for j in range(28):		
		data[i][j]=min(max(udata[i][j][3], 0), 1)*255

#data = data * 255

img1 = io.imshow(data)



io.show()

result = float(model.predict(np.array([data])))
intresult = int(result+0.5)

resrange = abs(intresult - result)
percvalid = 100 - ((resrange / 0.5) * 100)

print('Result', intresult, 'Validness', percvalid, sep='\n')










