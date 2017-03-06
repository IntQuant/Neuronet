class Basic():
    def __init__(self):
        self.objects = []
    def start_screen(self):
        while len(self.objects)<100:
            objsize = random(5, 30)
            self.objects.append([random(width), random(height), objsize, objsize, (randomGaussian()-0.5)*3, (randomGaussian()-0.5)*3])
        background(0)
        for object in self.objects:
            ellipse(*object[:4])
            object[0] += object[4]
            object[1] += object[5]  
        for i, object in enumerate(list(self.objects)):
            if object[0]<0 or object[0]>width or object[1]<0 or object[1]>height:
                del self.objects[i]
                break
                
            
    