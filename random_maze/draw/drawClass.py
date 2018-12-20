# this is the super class

import pygame
from colors import *

class Draw(object):
    screenSize = width, height = 640, 480
    surface = pygame.display.get_surface()

    origin = originX, originY = 50, 50
    mazeWidth, mazeHeight = 400, 400
    wallLength = 20

    # this is newly added
    color = goodBLUE
