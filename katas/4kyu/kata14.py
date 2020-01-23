"""
Codewars 4 kyu kata: Conway's Game of Life - Unlimited Edition
URL: https://www.codewars.com/kata/52423db9add6f6fc39000354/python
"""


RULES = [[3], [2, 3]]


def neighbours(cells, x, y):
    return sum(cells[x + x1][y + y1] for y1 in (-1, 0, 1) for x1 in (-1, 0, 1) if 0 <= x + x1 < len(cells) and
               0 <= y + y1 < len(cells[x])) - cells[x][y]

def crop(cells):
    while not any(cells[0]):
        del cells[0]
    while not any(cells[-1]):
        del cells[-1]
    while not any(c[0] for c in cells):
        cells = [c[1:] for c in cells]
    while not any(c[-1] for c in cells):
        cells = [c[:-1] for c in cells]
    return cells

def get_generation(cells, generations):
    for _ in xrange(generations):
        tmp = [[0 for _ in xrange(len(cells[0]) + 2)]]
        for row in cells:
            tmp.append([0] + row[:] + [0])
        tmp.append([0 for _ in xrange(len(cells[0]) + 2)])
        cells = [row[:] for row in tmp]

        for x in xrange(len(cells)):
            for y in xrange(len(cells[x])):
                tmp[x][y] = 1 if neighbours(cells, x, y) in RULES[cells[x][y]] else 0

        cells = crop(tmp)

    return cells

