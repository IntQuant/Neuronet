"""96*96 to 32*32 image converter"""

from pathlib import Path
from pyglet import image
import random
import numpy as np
np.set_printoptions(threshold=np.nan)

global found
globals()['found'] = []
def getIntensityMap(rpath):
    pic = image.load(rpath).get_image_data()    
    picformat = 'RGBA'
    pitch = pic.width * len(picformat)
    pixels = pic.get_data(picformat, pitch)    
    arr = np.empty((96, 96))
    for ij in range(len(pixels)//4):
        i = ij*4
        arr[ij//96][ij%96] = (pixels[i]+pixels[i+1]+pixels[i+2]+1) * pixels[i+3]    
    return arr


def convert(rpath, toparam, num):    
    arr = getIntensityMap(rpath)
    arrr = np.zeros((32, 32))    
    for i in range(96):
        for j in range(96):
            arrr[i//3][j//3] += arr[i][j]
    treshold = arrr.sum() / (32*32)    
    arrr = arrr > treshold
    imagestring = ''
    for i in arrr:
        for j in i:
            if j:
                imagestring = imagestring + '0'
            else:
                imagestring = imagestring + '1'

    globals()['found'].append((imagestring, toparam, arrr.sum(), rpath))




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
    #print(i[3])	#Path
    #print(i[2])    #Sum
    print(i[1])     #Number
    print(i[0])     #Image
    


