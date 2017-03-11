import os

cwd = os.getcwd() + '/data/'

class Conv():
    def __init__(self):
        print('Initiating convolution module')
         #edge detection
        self.kernel = [
                       [-1, -1, -1],
                       [-1, 8, -1],
                       [-1, -1, -1],
                       ]
        
        """
        self.kernel = [
                       [0.1125, 0.1125, 0.1125],
                       [0.1125, 0.1, 0.1125],
                       [0.1125, 0.1125, 0.1125],                       
                       ]
        """
        #self.kernel = [[.1111111111111111]*3]*3
        print('Loading image')
        image = requestImage(cwd + 'apple.jpg')
        while image.width == 0:
            delay(10)
        print('Loading pixels')
        image.loadPixels()
        print('Transfering pixels')
        self.image = image.pixels
        self.xsize = image.width 
        self.ysize = image.height
        
        self.conv = [[None]*image.height for i in range(image.width)]
        
        print('Done')
        
    def Convolve_all(self):
        for i in range(self.xsize):
            for j in range(self.ysize):
                self.Convolve(i, j)
    def get(self, x, y):
        pos = x + y * self.xsize
        return self.image[pos]
    def Viev_Convolution(self):
        background(0)
        stroke(255)
        fill(0x0f, 0xf0, 0xff)
        textSize(32)
        text(repr(self.kernel), 40, 40)
        translate(150, 150)
        for i in xrange(1, self.xsize-1):
            for j in xrange(1, self.ysize-1):
                col = self.get(i, j)
                stroke(col)          
                fill(col)
                point(i, j)
                concol = self.Convolve(i, j, mode=True) 
                stroke(concol)
                point(i+300, j)
                
                stroke((blue(concol) + green(concol) + red(concol)) / 3)
                
                point(i, j+300)
        for i in xrange(1, (self.xsize-1)//2):
            for j in xrange(1, (self.ysize-1)//2):
                conv1 = self.Convolve(i*2, j*2)
                conv2 = self.Convolve(i*2+1, j*2)
                conv3 = self.Convolve(i*2, j*2+1)
                conv4 = self.Convolve(i*2+1, j*2+1)
                col = max(conv1, conv2, conv3, conv4)
                stroke(col)
                point(i*2+300, j*2+300)
                point(i*2+300+1, j*2+300)
                point(i*2+300, j*2+300+1)
                point(i*2+300+1, j*2+300+1)
                point(i+200, j+200)
        
        noLoop()
                
                
                
    def Convolve(self, i, j, mode=False):
        offset = 0
        if self.conv[i][j] is not None:
            if mode:
                return color(*self.conv[i][j])
            else:
                return sum(self.conv[i][j])/3
        convr = [
        red(self.get(i, j)) * self.kernel[1][1]+offset,
        red(self.get(i+1, j)) * self.kernel[2][1]+offset,
        red(self.get(i-1, j)) * self.kernel[0][1]+offset,
        red(self.get(i, j+1)) * self.kernel[1][2]+offset,
        red(self.get(i, j-1)) * self.kernel[1][0]+offset,
        red(self.get(i+1, j+1)) * self.kernel[2][2]+offset,
        red(self.get(i-1, j-1)) * self.kernel[0][0]+offset,
        red(self.get(i+1, j-1)) * self.kernel[2][0]+offset,
        red(self.get(i-1, j+1)) * self.kernel[0][2]+offset,
        ]
        convg = [
        green(self.get(i, j)) * self.kernel[1][1]+offset,
        green(self.get(i+1, j)) * self.kernel[2][1]+offset,
        green(self.get(i-1, j)) * self.kernel[0][1]+offset,
        green(self.get(i, j+1)) * self.kernel[1][2]+offset,
        green(self.get(i, j-1)) * self.kernel[1][0]+offset,
        green(self.get(i+1, j+1)) * self.kernel[2][2]+offset,
        green(self.get(i-1, j-1)) * self.kernel[0][0]+offset,
        green(self.get(i+1, j-1)) * self.kernel[2][0]+offset,
        green(self.get(i-1, j+1)) * self.kernel[0][2]+offset,
        ]
        convb = [
        blue(self.get(i, j)) * self.kernel[1][1]+offset,
        blue(self.get(i+1, j)) * self.kernel[2][1]+offset,
        blue(self.get(i-1, j)) * self.kernel[0][1]+offset,
        blue(self.get(i, j+1)) * self.kernel[1][2]+offset,
        blue(self.get(i, j-1)) * self.kernel[1][0]+offset,
        blue(self.get(i+1, j+1)) * self.kernel[2][2]+offset,
        blue(self.get(i-1, j-1)) * self.kernel[0][0]+offset,
        blue(self.get(i+1, j-1)) * self.kernel[2][0]+offset,
        blue(self.get(i-1, j+1)) * self.kernel[0][2]+offset,
        ]
        self.conv[i][j] = [sum(convr), sum(convg), sum(convb)]
        if mode:
            return color(sum(convr), sum(convg), sum(convb))
        else:
            return (sum(convr) + sum(convg) + sum(convb)) / 3
        
    
    
    
    
    
    
    """
     Marks
     
     
     
     
     [
      [[0,1,2],[3,4,5],[6,7,8]],
      [[9,10,11],[12,13,14],[15,16,17]],
      ]
    -> [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14,15, 16, 17]
    
    
    
    
    
    """