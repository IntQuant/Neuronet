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
from pyglet import image

def getIntensityMap(rpath):
    pic = image.load(rpath).get_image_data()        
    picformat = 'RGBA' #ABGR
    pitch = pic.width * len(picformat)
    pixels = pic.get_data(picformat, pitch)
    pixels = bytes(reversed(pixels))
    arr = np.empty((pic.width, pic.height))
    for ij in range(len(pixels)//4):
        i = ij*4
        arr[ij//pic.height][ij%pic.height] = (pixels[i+1]+pixels[i+2]+pixels[i+3]+1) * pixels[i]    
    return (pic.width, pic.height, arr)
def convert(rpath):    
    IM = getIntensityMap(rpath)
    width = IM[0]
    height = IM[1]
    dwidth = width / 28
    dheight = height / 28
    arr = IM[2]
    arrr = np.zeros((28, 28))    
    for i in range(width):
        for j in range(height):
            arrr[math.floor(i/dwidth)][math.floor(j/dheight)] += arr[i][j]
    treshold = arrr.sum() / (28*28)     
    arrr = arrr / (dwidth*dheight)
    imagelist = []
    for i in arrr:
        for j in i:            
                imagelist.append(max(0, j))
    return imagelist

parser = argparse.ArgumentParser(description='Neuronet for reading numbers from images')
parser.add_argument('Path', type=str, help='Path to predit from')

args = parser.parse_args()

model = Sequential()
model.add(Reshape((28,28),input_shape=(28*28,)))
model.add(LSTM(150, consume_less='gpu', input_shape = (28, 28)))
model.add(Dense(output_dim=50))
model.add(Activation("relu"))
model.add(Dense(output_dim=1))
model.add(Activation("relu"))

model.load_weights('Weights.hd5')

for e, i in enumerate((convert(args.Path))):
	if e%28==0:
		print()
	print(int(i), end='\t')

data = np.array([convert(args.Path)])

print(float(model.predict(data)))










