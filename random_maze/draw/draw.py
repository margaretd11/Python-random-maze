# this is the main draw function

import sys
import pygame

pygame.init()
screen = pygame.display.set_mode((640,480))

from colors import *
import background
import outerWall
import allWalls
from lib.list import *


def init(data, doorMap):
        data.bg = background.Background(goodBLUE)
        data.boundary = outerWall.OuterWall(WHITE)
        data.walls = allWalls.AllWalls(doorMap, WHITE)

def redrawAll():
    data.bg.draw()
    data.boundary.draw()
    data.walls.draw()

# execution
class Struct(object): pass
data = Struct()

doorMap = make3DList(20, 20, 3, 0)
doorMap[0][0][0], doorMap[0][0][1] = 1, 1

init(data, doorMap)
redrawAll()

# bellow is for testing
while 1:
    for event in pygame.event.get():
        if event.type in (pygame.QUIT, pygame.KEYDOWN):
            sys.exit()
    pygame.display.flip()
