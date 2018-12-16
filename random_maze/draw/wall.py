# wall of the maze

import pygame
import drawClass

class Wall(drawClass.Draw):

    # Model
    def __init__(self, start, dir, color):
        self.start = start
        self.dir = dir
        self.color = color
        if (dir == 'h'):
            self.end = (start[0] + self.wallLength, start[1])
        if (dir == 'v'):
            self.end = (start[0], start[1] + self.wallLength)

    # View
    def draw(self):
        pygame.draw.line(self.surface, self.color, self.start, self.end, 2)

    # no Controller
