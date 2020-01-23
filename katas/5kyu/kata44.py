"""
Codewars 5 kyu kata: The Clockwise Spiral
URL: https://www.codewars.com/kata/536a155256eb459b8700077e/python
"""


def _nextPos(pos, dir):
    if dir == 0:
        return pos[0], pos[1] + 1
    elif dir == 1:
        return pos[0] + 1, pos[1]
    elif dir == 2:
        return pos[0], pos[1] - 1
    elif dir == 3:
        return pos[0] -1 , pos[1]

def createSpiral(n):
    try:
        int(n)
    except:
        return []

    result = [[0 for x in xrange(n)] for y in xrange(n)]
    val = 1
    init = 1
    dir = 0
    pos = (0,-1)

    for i in reversed(xrange(n)):
        while init < 2:
            for _ in xrange(i+1):
                pos = _nextPos(pos, dir)
                result[pos[0]][pos[1]] = val
                val+= 1
            dir = (dir + 1) % 4
            init += 1
        init = 0

    return result

