# draws the maze

import sys
import pygame
import drawClass

pygame.init()
screen = pygame.display.set_mode(drawClass.Draw.screenSize)

from colors import *
import background
import outerWall
import allWalls
import maze1
import dot
# import drawClass


def init(data, doorMap):
    data.bg = background.Background(goodBLUE)
    data.boundary = outerWall.OuterWall(WHITE)
    data.walls = allWalls.AllWalls(doorMap, WHITE)
    # testing dot
    data.dot = dot.Dot(110, 110)

def redrawAll():
    data.bg.draw()
    data.boundary.draw()
    data.walls.draw()
    data.dot.draw()

# execution
class Struct(object): pass
data = Struct()

doorMap = maze1.buildMaze1()

init(data, doorMap)
redrawAll()

# bellow is for testing
while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    pygame.display.flip()