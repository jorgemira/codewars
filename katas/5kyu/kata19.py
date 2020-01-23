"""
Codewars 5 kyu kata: Sudoku Solver
URL: https://www.codewars.com/kata/5296bc77afba8baa690002d7/python
"""


ALL = set(xrange(1, 10))


def possibles(puzzle, x, y):
    a, b = x / 3 * 3, y / 3 * 3
    taken = set(puzzle[x] +  # Horizontal
                [puzzle[i][y] for i in xrange(9)] +  # Vertical
                [puzzle[x2][y2] for y2 in xrange(b, b + 3) for x2 in xrange(a, a + 3)])  # Quadrant
    return ALL - taken


def sudoku(puzzle, pos=0):
    """return the solved puzzle as a 2d array of 9 x 9"""

    if pos == 81:
        return puzzle

    x, y = pos / 9, pos % 9

    if not puzzle[x][y]:  
        for i in possibles(puzzle, x, y):
            puzzle[x][y] = i
            tmp = sudoku(puzzle, pos + 1)
            if tmp:
                return tmp
            else:
                puzzle[x][y] = 0

        return None
    else:
        return sudoku(puzzle, pos + 1)

