"""
Codewars 4 kyu kata: Matrix Determinant
URL: https://www.codewars.com/kata/52a382ee44408cea2500074c/python
"""


def minor(matrix, i):
    return [[matrix[x][y] for y in xrange(0, len(matrix[x])) if i != y] for x in xrange(1, len(matrix))]

def determinant(matrix):
    return matrix[0][0] if len(matrix) == 1 else sum(v * determinant(minor(matrix, i)) * (-1) ** i for i, v in enumerate(matrix[0]))

