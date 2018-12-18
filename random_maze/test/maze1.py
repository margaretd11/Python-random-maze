# maze1

from lib.list import *

def buildMaze1():
    maze1 = make3DList(20, 20, 2, 1)
    for j in range(len(maze1[0])):
        maze1[0][j][1] = 0
    maze1[0][len(maze1[0])-1][0] = 0
    print(maze1)
    return maze1
