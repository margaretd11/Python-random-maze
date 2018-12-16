# this is the super class

import pygame

class Draw(object):
    screenSize = width, height = 640, 480
    screen = pygame.display.set_mode(screenSize)
    surface = pygame.display.get_surface()

    origin = originX, originY = 50, 50
    mazeWidth, mazeHeight = 400, 400
    wallLength = 20
