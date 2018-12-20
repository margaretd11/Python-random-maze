# the main file

import sys
import pygame

pygame.init()
assert (pygame.cdrom.get_init)
screen = pygame.display.set_mode((640,480))
pygame.key.set_repeat(100, 100)

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
    data.dot = dot.Dot(60, 60, doorMap)

def redrawAll():
    data.bg.draw()
    data.boundary.draw()
    data.walls.draw()
    data.dot.draw()



# execution
class Struct(object): pass
data = Struct()

doorMap = maze.buildMaze2()

init(data, doorMap)
redrawAll()


# main loop
while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            pressKeys = pygame.key.get_pressed()
            if pressKeys[113]:  sys.exit()
            if pressKeys[119]:  # w
                data.dot.move('u')
                data.dot.draw()
            if pressKeys[115]:  # s
                data.dot.move('d')
                data.dot.draw()
            if pressKeys[97]:  # a
                data.dot.move('l')
                data.dot.draw()
            if pressKeys[100]:  # d
                data.dot.move('r')
                data.dot.draw()
    pygame.display.flip()

