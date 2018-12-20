# mazes for testing

from lib.list import *

def buildMaze1():
    maze1 = make3DList(20, 20, 2, 1)
    for j in range(len(maze1[0])):
        maze1[0][j][1] = 0  # right wall is 1
    maze1[0][len(maze1[0])-1][0] = 0    # down wall is 0
    return maze1


def buildMaze2():
    maze2 = make3DList(20, 20, 2, 1)
    for j in range(len(maze2[0])):
        maze2[0][j][1] = 0  # right wall is 1
    maze2[0][len(maze2[0])-1][0] = 0    # down wall is 0
    maze2[0][5][0] = 0
    maze2[1][5][0] = 0
    maze2[1][6][0] = 0
    maze2[2][6][0] = 0
    maze2[2][5][1] = 0
    return maze2

