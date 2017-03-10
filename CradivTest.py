"""
________  _____	 _____  _________
    |     | 	 |			|
    |	  +____  +____		|
    |	  |			 |		|
    |     +____	 ____+ 		|
"""
from CharDiv import NumberDivide
import numpy as np
from skimage import io, transform, draw

io.use_plugin('matplotlib')

uimage = io.imread('/home/iquant/Документы/1324.png') * 255

image = np.empty((uimage.shape[0], uimage.shape[1]), dtype = np.uint8)

for i in range(uimage.shape[0]):
	for j in range(uimage.shape[1]):
		image[i][j] = uimage[i][j][3]



print(image.shape)

ND = NumberDivide()

matrix, objects = ND.Hightlight(image)

coords = ND.Divide(matrix)

for (x1, y1, x2, y2) in coords:
	print(x1,y1,x2,y2)
	io.imshow(transform.resize(image[x1:x2,y1:y2], output_shape=(28, 28)))
	io.show()


