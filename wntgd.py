import sys
from keras.datasets import mnist
import numpy as np
import random
from INeuronet import GetModel
from keras.optimizers import SGD
from skimage import transform as tf
print('Loading data')
(X_train, y_train), (X_test, y_test) = mnist.load_data()
print(X_train.shape)

seed = 7
np.random.seed(seed)
random.seed(seed)

#testsx = X_train
testsy = y_train

#testsx = np.array(testsx)
y_test = y_test.reshape((10000, 1, 1))
model = GetModel.getmodel()
print('resizing')

testsx = np.empty((60000, 32, 32), dtype=np.uint8)
Xtest = np.empty((10000, 32, 32), dtype=np.uint8)

for i in range(60000):
	testsx[i] = tf.reshape(X_train[i], output_shape=(32, 32))

for i in range(10000):
	Xtest[i] = tf.reshape(X_test[i], output_shape=(32, 32))

currentbath = 0

print('-'*50)

csgd = SGD(lr=1e-4, momentum=0.9)

#print(model.predict(testsx).shape)

model.compile(
             loss='mean_absolute_error',
             optimizer=csgd,
             )
iteration = 0
while True:
	print(iteration)
	for i in range(1000):		
		x = np.array([testsx[currentbath+i] for i in range(10)]).reshape((10, 28, 28))
		y = np.array([testsy[currentbath+i] for i in range(10)]).reshape((10, 1, 1, 1))
		currentbath = (currentbath + 10) % (len(testsy)-11)
		model.train_on_batch(x, y)
		if i%100==0:
			print('=', end='')		
	print()
	print('Testing')
	predicted = model.predict(Xtest)
	print('Calculating perfomance')
	perfomance = [0]*10
	irrperf = [0]*10
	numcount = [0]*10
	totalperc = 0
	for answer, predicted in zip(y_test, predicted):
		if int(float(predicted)+0.5) == int(answer):
			perfomance[int(answer)] += 1
		else:
			irrperf[int(answer)] += 1
		numcount[int(answer)] += 1
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

	with open('History', 'a') as history:
		print(iteration, totalperc/10, file=history)
	if iteration % 5 == 0:
		model.save_weights('Weights/Weights-auto'+str(iteration)+'.hd5')
	iteration += 1

model.save_weights('Weights.hd5')




