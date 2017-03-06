from image import GI

class Conv():
    def __init__(self):
        self.kernel = [
                       [-1, -1, -1],
                       [-1,  8, -1],
                       [-1, -1, -1],
                       ]
        self.image = GI()
        self.size = 32
        self.channels = 3
    def get(self, x, y):
        pos = x * self.size * self.channels + y * self.channels
        return self.image[pos: pos+2]
    def Viev_Convolution(self):
        background(0)
        stroke(255)
        noLoop()
        for i in range(self.size):
            for j in range(self.size):
                col = self.get(i, j)
                stroke(*col)          
                fill(*col)
                
                rect(i*5, j*5, i*5+5, j*5+5)
    
    
    
    
    
    
    """
     Marks
     
     
     
     
     [
      [[0,1,2],[3,4,5],[6,7,8]],
      [[9,10,11],[12,13,14],[15,16,17]],
      ]
    -> [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14,15, 16, 17]
    
    
    
    
    
    """