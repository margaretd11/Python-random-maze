# Generating random maze based on 122 lecture note
# Note: this algorithm is edge-centric

import random
from unionfind import *
import list

size = 20

# helper
def id(row, col):
    return row * size + col

def row_col(id):
    return (id // size, id % size)

# returns a RANDOM sequence of edges
def getEdge():
    A = []
    for row in range(size - 1):
        for col in range(size - 1):
            # randomly insert
            index = random.randint(0, len(A))
            A.insert(index, (id(row, col), id(row, col+1)))
            index = random.randint(0, len(A))
            A.insert(index, (id(row, col), id(row+1, col)))
    for row in range(size - 1):
        index = random.randint(0, len(A))
        A.insert(index, (id(row, size-1), id(row+1, size-1)))
    for col in range(size - 1):
        index = random.randint(0, len(A))
        A.insert(index, (id(size-1, col), id(size-1, col+1)))
    assert(len(A) == 2 * (size - 1) * size)
    return A

# create a spanning tree
def connect(E):
    UF = UF_new(size*size)
    doors = []
    e = 0
    while e < size*size - 1:
        edge = E.pop()
        if union(UF, edge[0], edge[1]):
            e += 1
            doors.append((edge))
    return doors

# convert into 3D-list
def drawMap(doors):
    doorMap = list.make3DList(size, size, 2, 1)
    for edge in doors:
        coord_a = row_col(edge[0])
        if edge[1]-edge[0] == 1:
            doorMap[coord_a[0]][coord_a[1]][1] = 0
        else:
            assert(edge[1]-edge[0] == size)
            doorMap[coord_a[0]][coord_a[1]][0] = 0
    return doorMap

def createMaze():
    E = getEdge()
    return drawMap(connect(E))