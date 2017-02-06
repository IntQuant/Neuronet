"""
\Project-Worm
 \Server
  \field.py
"""
#import operator
import itertools
from array import array
class matrix:
    """2d array """
    def __init__(self, size):
        self.size = size
        self.x = size[0]
        self.y = size[1]
        self.array = array('H', itertools.repeat(0, self.x*self.y))
        #H is 2-bytes unsigned integer
    def __getitem__(self, coordinate):
        x = coordinate[0]
        y = coordinate[1]
        flatcoord = x*self.y+y
        return self.array[flatcoord]
    def __setitem__(self, start, value):
        x = start[0]
        y = start[1]
        flatcoord = x*self.y+y
        self.array[flatcoord] = value
    def getsize(self):
        """Return size of matrix"""
        return self.size
    def flat(self):
        """Returns the underlying array object"""
        return self.array
class Field:
    def __init__(self, size):
        self.size=size
        self.x = size[0]
        self.y = size[1]
        self.matrix = []
    def update(self):
        pass
    def getsize(self):
        """Return size of underlying matrix object"""
        return self.size
    def getmatrix(self):
        """Returns underlying matrix object"""
        return self.matrix

matrx = matrix((10, 10))
matrx[(0, 0)] = 1
print(matrx[(0, 0)]) 
