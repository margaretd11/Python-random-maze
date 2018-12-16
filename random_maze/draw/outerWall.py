# boundaries of the maze

import pygame
from colors import *
import drawClass

class OuterWall(drawClass.Draw):
    # Model
    def __init__(self, color):
        self.color = color

    # View
    def draw(self):
        pygame.draw.line(self.surface, self.color, self.origin, (self.origin[0] + self.mazeWidth, self.origin[1]), 4)
        pygame.draw.line(self.surface, self.color, self.origin, (self.origin[0], self.origin[1] + self.mazeHeight), 4)
        pygame.draw.line(self.surface, self.color, (self.origin[0] + self.mazeWidth, self.origin[1]),
                         (self.origin[0] + self.mazeWidth, self.origin[1] + self.mazeHeight), 4)
        pygame.draw.line(self.surface, self.color, (self.origin[0], self.origin[1] + self.mazeHeight),
                         (self.origin[0] + self.mazeWidth, self.origin[1] + self.mazeHeight), 4)

    # no Controller