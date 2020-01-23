"""
Codewars 6 kyu kata: Sudoku Solution Validator
URL: https://www.codewars.com/kata/529bf0e9bdf7657179000008/python
"""


def validSolution(board):
    nums = set(xrange(1, 10))
    if any(set(row) != nums for row in board):
        return False
    if any(set(board[row][i] for row in xrange(9)) != nums for i in xrange(9)):
        return False
    for x, y in ((x * 3, y * 3) for y in xrange(3) for x in xrange(3)):
        if set(board[x2][y2] for y2 in xrange(y, y + 3) for x2 in xrange(x, x + 3)) != nums:
            return False
    return True

