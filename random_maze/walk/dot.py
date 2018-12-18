# dot (represents current location) in the maze

import pygame
from draw.colors import *
import walkClass

class Dot(walkClass.Walk):
    # Model
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # View
    def draw(self):
        pygame.draw.circle(self.surface, RED, (self.x, self.y), 10, 0)

    # Controller
    def move(self, dir):
        if(dir == 'l'): self.x -= self.speed
        if(dir == 'r'): self.x += self.speed
        if(dir == 'u'): self.y -= self.speed
        if(dir == 'd'): self.y += self.speed