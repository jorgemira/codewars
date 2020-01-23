"""
Codewars 3 kyu kata: Hard Sudoku Solver
URL: https://www.codewars.com/kata/55171d87236c880cea0004c6/python
"""


ALL = set(xrange(1, 10))


def possibles(puzzle, x, y):
    a, b = x / 3 * 3, y / 3 * 3
    taken = set(puzzle[x] +  # Horizontal
                [puzzle[i][y] for i in xrange(9)] +  # Vertical
                [puzzle[x2][y2] for y2 in xrange(b, b + 3) for x2 in xrange(a, a + 3)])  # Quadrant
    return ALL - taken


def solve(puzzle, pos=0):
    """return the solved puzzle as a 2d array of 9 x 9"""
    if pos == 81:
        return puzzle

    x, y = pos / 9, pos % 9

    if not puzzle[x][y]:
        for i in possibles(puzzle, x, y):
            puzzle[x][y] = i
            tmp = solve(puzzle, pos + 1)
            if tmp:
                return tmp
        puzzle[x][y] = 0
        return None
    else:
        return solve(puzzle, pos + 1)

        

ALL = set(xrange(1, 10))


def possibles(puzzle, x, y):
    a, b = x / 3 * 3, y / 3 * 3
    taken = set(puzzle[x] +  # Horizontal
                [puzzle[i][y] for i in xrange(9)] +  # Vertical
                [puzzle[x2][y2] for y2 in xrange(b, b + 3) for x2 in xrange(a, a + 3)])  # Quadrant
    return ALL - taken


def solve(puzzle, pos=0):
    """return the solved puzzle as a 2d array of 9 x 9"""
    if pos == 81:
        return puzzle

    x, y = pos / 9, pos % 9

    if not puzzle[x][y]:
        for i in possibles(puzzle, x, y):
            puzzle[x][y] = i
            tmp = solve(puzzle, pos + 1)
            if tmp:
                return tmp
        puzzle[x][y] = 0
        return None
    else:
        return solve(puzzle, pos + 1)

