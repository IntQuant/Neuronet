class Prepare:
	@staticmethod
	def get():
		import numpy as np
		from skimage import transform as tf
		from keras.datasets import mnist
		from keras.utils import np_utils
		(X_train, y_train), (X_test, y_test) = mnist.load_data()
		
		outp = np.zeros((60000, 10))
		testout = np.zeros((10000, 10))
		
		print('Step |')
		for i in range(60000):
			outp[i][y_train[i]] = 1
		print('Step ||')
		for i in range(10000):
			testout[i][y_test[i]] = 1
		
		return X_train.reshape(60000, 28, 28, 1), outp, X_test.reshape(10000, 28, 28, 1), testout
		
		
