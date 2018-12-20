# draws the maze

import sys
import pygame

pygame.init()
assert (pygame.cdrom.get_init())
screen = pygame.display.set_mode((640,480))

from drawClass import *
from colors import *
import background
import outerWall
import allWalls
import dot
import maze


def init(data, doorMap):
    data.bg = background.Background(goodBLUE)
    data.boundary = outerWall.OuterWall(WHITE)
    data.walls = allWalls.AllWalls(doorMap, WHITE)
    # testing dot
    data.dot = dot.Dot(60, 60)

def redrawAll():
    data.bg.draw()
    data.boundary.draw()
    data.walls.draw()
    data.dot.draw()



# execution
class Struct(object): pass
data = Struct()

doorMap = maze.buildMaze1()

init(data, doorMap)
redrawAll()

# bellow is for testing
while 1:
    for event in pygame.event.get():
        if event.type in (pygame.QUIT, pygame.KEYDOWN):
            sys.exit()
    pygame.display.flip()