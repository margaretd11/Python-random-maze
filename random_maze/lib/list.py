# some functions for list manipulation

def make3DList(a, b, c, x):
    res = []
    for row in range(a):
        tmp = []
        for col in range(b):
            tmp += [[x]*c]
        res += [tmp]
    return res