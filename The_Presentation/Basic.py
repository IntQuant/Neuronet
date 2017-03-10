import os
cwd = os.getcwd() + '/data/'
class Basic():
    def __init__(self):
        self.objects = []
        self.images = {}
    def bg(self):
        while len(self.objects)<100:
            objsize = random(5, 30)
            self.objects.append([random(width), random(height), objsize, objsize, (randomGaussian()-0.5)*0.5, (randomGaussian()-0.5)*0.5])
        background(0)
        for object in self.objects:
            fill(50, 50, 255)
            ellipse(*object[:4])
            object[0] += object[4]
            object[1] += object[5]  
        for i, object in enumerate(list(self.objects)):
            if object[0]<0 or object[0]>width or object[1]<0 or object[1]>height:
                del self.objects[i]
                break
        
    def show_image(self, name):
        self.bg()
        if not name.startswith('img_'):
            return False
        if not (name in self.images):
            print('Loading', name)
            print('From', cwd + name[4:] + '.png')
            self.images[name] = requestImage(cwd + name[4:] + '.png')
            while self.images[name].width == 0:
                delay(10)
            print('Loaded')
        imageMode(CENTER)
        image(self.images[name], width//2, height//2)
        
        
        
                
            
    