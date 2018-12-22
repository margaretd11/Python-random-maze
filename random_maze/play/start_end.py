# initialize start and end position

import sys
import random
import pygame
import dot
import list

from drawClass import *

def start(a):
    x = Draw.originX + Draw.wallLength//2 + random.randint(0, Draw.numCols-1)*Draw.wallLength
    y = Draw.originY + Draw.wallLength//2 + random.randint(0, Draw.numRows-1)*Draw.wallLength
    a.setPos(x, y)

def succeed(a, x, y):
    if a.x == x and a.y == y: return True
    return False
