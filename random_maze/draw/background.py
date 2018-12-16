# background of the maze

import pygame
import drawClass

class Background(drawClass.Draw):
    # Model
    def __init__(self, color):
        self.color = color

    # View
    def draw(self):
        pygame.draw.rect(self.surface, self.color, [0, 0, self.width, self.height])

    # no Controller
