import numpy as np

class ImageProcess2D:
	def __init__(self, image):
		if type(image) != 'ndarray' | len(image.shape) != 2:
			raise TypeError('Wrong image type or shape')
		self.image = image
		self.x = image.shape[0]
		self.y = image.shape[1]
	def findCentre(self, maincolor=255):
		halfx = x / 2
		halfy = y / 2
		centre =  (0, 0)
		for i in range(int(-halfx), int(halfx+0.5)):
			for j in range(int(-halfy, int(halfy+0.5))):
				value = self.image[i+halfx][j+halfy]
				
	def process(self, x, y):
		"""Centeres the image and resizes it"""
	    xmultiplier = x / self.x
	    ymultiplier = y / self.y
	    
