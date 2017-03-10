DO_NOT_SPAM = True


def lprint(*args, **kwargs):
	if not DO_NOT_SPAM:
		print(*args, **kwargs)

lprint('Importing time')
import time

stime = time.time()

if DO_NOT_SPAM:
	import sys
	sys.stderr = open('/dev/null','w')

lprint('Importing slimage')
from skimage import io, transform
lprint('Importing numpy')
import numpy as np
lprint('Importing model')
from INeuronet import GetModel
lprint('Importing dataset')
from keras.datasets import mnist
lprint('Importing datagen')
from keras.preprocessing.image import ImageDataGenerator as datagenc
lprint('Complited in')
lprint(time.time()-stime, 'sec')

lprint('Loading data')
(X_train, y_train), (X_test, y_test) = mnist.load_data()

lprint('Loading model')
model = GetModel.getmodel()

lprint('Loading weights')
model.load_weights('Weights.hd5')

lprint('Setting up datagen')
datagen = datagenc(
 rotation_range = 20,
 zoom_range = [0.9, 1.2],
 width_shift_range=0.2,
 height_shift_range=0.2,  
)
"""
flow = datagen.flow(X_train.reshape(-1, 28, 28, 1), y_train, batch_size = 1)
for i in flow:
	io.imshow(i[0].reshape(28, 28)/255)	
	print(i[1][0], model.predict_classes(i[0], verbose=0)[0])
	io.show()
	"""


counter = 0
print('Predicting')
predicted = model.predict(X_test.reshape(10000, 28, 28, 1))

print('Shape is', predicted.shape)
for ip in range(10000):
	resultsl = predicted[ip]
	
	cmax = 0
	for i, v in enumerate(resultsl):
		if v > resultsl[cmax]:
			cmax = i
	if y_test[ip] == cmax:
		counter+=1		

print(counter)
print(counter / 10000, 'part of all')

barcount = int(counter/250)

print('['+'='*barcount+' '*(40 - barcount)+']')

io.use_plugin('matplotlib')

time.sleep(1)




