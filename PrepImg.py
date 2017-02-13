class Prepare:
	@staticmethod
	def get():
		import numpy as np
		from skimage import transform as tf
		from keras.datasets import mnist
		from keras.utils import np_utils
		(X_train, y_train), (X_test, y_test) = mnist.load_data()
		print('resizing')
		testsx = np.empty((60000, 4, 32, 32), dtype=np.uint8)
		outp = np.zeros((60000, 10))
		
		print('Step |')
		for i in range(60000):
			testsx[i] = tf.resize(X_train[i], output_shape=(4, 32, 32)) / 255
		for i in range(60000):
			outp[i][y_train[i]] = 1
		
		
		return testsx, outp
		
		
