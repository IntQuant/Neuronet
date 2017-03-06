import Basic as BC
import Convolutional as cv
basic = BC.Basic()
conv = cv.Conv()

screen = 'scr_convolve'

def setup():
    size(displayWidth, displayHeight)
    frameRate(1)


def draw():
    global screen
    if screen ==  'scr_start':
        basic.start_screen()
    elif screen =='scr_convolve':
        conv.Viev_Convolution()
    