import Basic as BC
import Convolutional as cv
import os

print(os.getcwd())

basic = BC.Basic()
conv = cv.Conv()

screens = [
    'img_Title',
    'img_targets-lite',
    'img_targets-full',
    'img_Neuronet-structure',
    'img_Dense-theory',
    'img_Convolution-theory',
    'img_Maxpooling-theory',
    'scr_convolve',
    'img_Demonstration'
    ]
screen = screens[0]
scrnum = 0

def keyPressed():
    global scrnum
    global screen
    global screens
    if key == 'n':
        scrnum += 1
    elif key == 'b':
        scrnum -= 1
    scrnum %= len(screens)
    screen = screens[scrnum]
    print(screen)
    loop()

def setup():
    size(800, 800)
    frameRate(60)


def draw():
    global screen
    if basic.show_image(screen):
        pass
    elif screen =='scr_convolve':
            conv.Viev_Convolution()
    