# the main file

import sys
import random
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
import start_end
import spanning


def init(data, doorMap):
    data.bg = background.Background(goodBLUE)
    data.boundary = outerWall.OuterWall(WHITE)
    data.walls = allWalls.AllWalls(doorMap, WHITE)
    data.dot = dot.Dot(60, 60, doorMap)
    start_end.start(data.dot)

def redrawAll():
    data.bg.draw()
    data.boundary.draw()
    data.walls.draw()
    data.dot.draw()

def end():
    x = Draw.originX + Draw.wallLength//2 + random.randint(0, Draw.numCols-1)*Draw.wallLength
    y = Draw.originY + Draw.wallLength//2 + random.randint(0, Draw.numRows-1)*Draw.wallLength
    pygame.draw.circle(Draw.surface, GREEN, (x,y), 5, 0)
    return (x, y)


# execution
class Struct(object): pass
data = Struct()

doorMap = spanning.createMaze()

init(data, doorMap)
redrawAll()

# end point
exit = end()

# main loop
while 1:
    if start_end.succeed(data.dot, exit[0], exit[1]):
        pygame.draw.rect(Draw.surface, BLUE, (exit[0]-Draw.wallLength//2, exit[1]-Draw.wallLength//2, Draw.wallLength, Draw.wallLength))
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
                doorMap = spanning.createMaze()
                init(data, doorMap)
                redrawAll()
                exit = end()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:  sys.exit()
            if event.key == pygame.K_UP:
                data.dot.move('u')
                data.dot.draw()
            if event.key == pygame.K_DOWN:
                data.dot.move('d')
                data.dot.draw()
            if event.key == pygame.K_LEFT:
                data.dot.move('l')
                data.dot.draw()
            if event.key == pygame.K_RIGHT:
                data.dot.move('r')
                data.dot.draw()
    pygame.display.flip()
