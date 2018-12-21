# union find interface

from contracts import *

def UF_new(n):
    return [-1] * n

def find(UF, a):
    requires(0 <= a and a < len(UF))
    while(a >= 0):
        id = a
        a = UF[id]
    assert(a < 0)
    return id

def connected(UF, a, b):
    return find(UF, a) == find(UF, b)

def union(UF, a, b):
    roota = find(UF, a)
    rootb = find(UF, b)
    if roota == rootb:  return False
    if UF[roota] < UF[rootb]:  # a is higher than b
        UF[rootb] = roota
    elif UF[roota] > UF[rootb]:  # b is higher than a
        UF[roota] = rootb
    else:
        UF[rootb] = roota
        UF[roota] -= 1
    return True

