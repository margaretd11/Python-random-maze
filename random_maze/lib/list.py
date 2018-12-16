# some functions for list manipulation

def make3DList(a, b, c):
    res = []
    for row in range(a):
        tmp = []
        for col in range(b):
            tmp += [[0]*c]
        res += [tmp]
    return res