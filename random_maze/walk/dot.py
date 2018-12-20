# dot (represents current location) in the maze

import pygame
from colors import *
import drawClass
import allWalls

class Dot(drawClass.Draw):
    # Model
    def __init__(self, x, y, doorMap):
        self.x = x
        self.col = (x-self.originX) // self.wallLength
        self.y = y
        self.row = (y-self.originY) // self.wallLength
        self.speed = self.wallLength
        self.doorMap = doorMap

    # View
    def draw(self):
        pygame.draw.circle(self.surface, RED, (self.x, self.y), 5, 0)

    # Controller
    def outbound(self, dir):
        if(dir == 'l'):
            return self.x == self.originX + self.wallLength // 2
        if(dir == 'r'):
            return self.x == self.originX + self.mazeWidth - self.wallLength // 2
        if(dir == 'u'):
            return self.y == self.originY + self.wallLength // 2
        if(dir == 'd'):
            return self.y == self.originY + self.mazeWidth - self.wallLength // 2

    def hitWall(self, dir):
        if(dir == 'l'):
            return self.doorMap[self.row][self.col-1][1]
        if(dir == 'r'):
            return self.doorMap[self.row][self.col][1]
        if(dir == 'u'):
            return self.doorMap[self.row-1][self.col][0]
        if(dir == 'd'):
            return self.doorMap[self.row][self.col][0]

    def move(self, dir):
        if self.outbound(dir) or self.hitWall(dir):  return
        pygame.draw.circle(self.surface, self.color, (self.x, self.y), 5, 0)
        if(dir == 'l'):
            self.x -= self.speed
            self.col = (self.x-self.originX) // self.wallLength
        if(dir == 'r'):
            self.x += self.speed
            self.col = (self.x-self.originX) // self.wallLength
        if(dir == 'u'):
            self.y -= self.speed
            self.row = (self.y-self.originY) // self.wallLength
        if(dir == 'd'):
            self.y += self.speed
            self.row = (self.y-self.originY) // self.wallLength
