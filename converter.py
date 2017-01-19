"""96*96 to 32*32 image converter"""

from pathlib import Path
from pyglet import image
import random
import numpy as np
np.set_printoptions(threshold=np.nan)

global found
globals()['found'] = []

def convert(rpath, toparam, num):
    pic = image.load(rpath).get_image_data()
    picformat = 'I'
    pitch = pic.width * len(picformat)
    pixels = pic.get_data(picformat, pitch)
    arr = np.empty((96, 96))
    arrr = np.zeros((32, 32))
    for i, element in enumerate(pixels):
        arr[i//96][i%96] = element
        #print(i//96, i%96, e)
    #print(e)
    #print(pixels[0])
    for i in range(96):
        for j in range(96):
            arrr[i//3][j//3] += arr[i][j]
    for i in range(32):
        for j in range(32):
            arrr[i][j] = arrr[i][j] // 9
    arrr = arrr > 128
    imagestring = ''
    for i in arrr:
        for j in i:
            if j:
                imagestring = imagestring + '0'
            else:
                imagestring = imagestring + '1'

    globals()['found'].append((imagestring, toparam))




def listFiles(lpath, cparam):
    p = lpath
    try:
        for i, x in enumerate(p.iterdir()):
            if not x.is_dir():
                convert(str(x), cparam, i)
    except BaseException:
        pass
for i in range(10):
    x = Path('./Data/'+str(i))
    listFiles(x, i)

fnd = globals()['found']

fnd = random.sample(fnd, len(fnd))
for i in fnd:
    print(i[1])
    print(i[0])


