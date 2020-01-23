"""
Codewars 4 kyu kata: Make a spiral
URL: https://www.codewars.com/kata/534e01fbbb17187c7e0000c6/python
"""


from itertools import cycle


DIRS = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def add(x, y):
    return x[0] + y[0], x[1] + y[1]


def in_(grid, coord):
    return 0 <= coord[0] < len(grid) and 0 <= coord[1] < len(grid)


def valid(grid, coord):
    count = 0
    if not in_(grid, coord):
        return False
    for d in DIRS:
        tmp = add(coord, d)
        count += grid[tmp[0]][tmp[1]] if in_(grid, tmp) else 0
    return count <= 1


def advance(grid, coord, direction, dirs):
    tmp = add(coord, direction)
    if not valid(grid, tmp):
        direction = next(dirs)
        return add(coord, direction), direction
    return tmp, direction


def spiralize(size):
    dirs = cycle(DIRS)
    grid = [[0 for _ in range(size)] for _ in range(size)]
    pos, direction = (0, 0), next(dirs)
    while valid(grid, pos):
        grid[pos[0]][pos[1]] = 1
        pos, direction = advance(grid, pos, direction, dirs)
    return grid

