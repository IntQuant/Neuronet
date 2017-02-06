import numpy as np
import sys

class matrixprocess:
	def __init__(self, treshold):
		self.x = 0
		self.y = 0
		self.treshold
		self.image = np.empty((self.x, self.y))
	def setsize(self, x, y):
		self.x = x
		self.y = y
		self.image = np.empty((self.x, self.y))
	def process(self. image):		
		if len(image.shape) != 2:
			raise TypeError('Object shape is not 2 dimensional')
		if image.shape != (x, y):
			print('Size is not equeval to set, setting image shape', file=sys.stderr)
			self.x, self.y = image.shape
		self.image = image
		point = [self.x // 2, self.y // 2]
		pointlu = list(point)
		pointld = list(point)
		pointru = list(point)
		pointrd = list(point)
		for i in range(0, self.x):
			for j in range(0, self.y:
				if self.image[i:j]>self.treshold:
					if pointlu[0]<i:
						pointlu[0] = i
					else:
						pointru[1] = max(pointlu[1], j)
					if pointru[0]>i:
						pointru[0] = i
					else:
						pointru[1] = min(pointru[1], j)
					
					if pointld[0]<i:
						pointld[0] = i
					else:
						pointld[1] = max(pointld[1], j)
					
					if pointrd[0]<i:
						pointrd[0] = i
					else:
						pointrd[1] = min(pointrd[1], j)
		return pointlu, pointld, pointru, pointrd

					
		
		
		
		
		
