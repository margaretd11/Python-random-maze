# all walls in the maze

import pygame
from contracts import *
import drawClass
import wall

class AllWalls(drawClass.Draw):
    # Model
    def __init__(self, doorMap, color):
        requires(self.mazeWidth % self.wallLength == 0)
        requires(self.mazeHeight % self.wallLength == 0)
        self.numRows = self.mazeHeight // self.wallLength
        self.numCols = self.mazeWidth // self.wallLength

        requires(len(doorMap) == self.numRows)
        requires(len(doorMap[0]) == self.numCols)
        self.doorMap = doorMap
        self.color = color

    # View
    def draw(self):         # consider the DOWN and RIGHT edge of each box
        for i in range(self.numRows):
            for j in range(self.numCols):
                if (self.doorMap[i][j][0]):      # DOWN
                    w = wall.Wall((self.originX + j*self.wallLength,
                                   self.originY + (i+1)*self.wallLength), 'h', self.color)
                    w.draw()
                if (self.doorMap[i][j][1]):      # RIGHT
                    w = wall.Wall((self.originX + (j+1)*self.wallLength,
                                   self.originY + i*self.wallLength), 'v', self.color)
                    w.draw()

    # Controller
    def changeMap(self, newMap):
        requires(len(newMap) == self.numRows)
        requires(len(newMap[0]) == self.numCols)
        self.doorMap = newMap