"""
Codewars 7 kyu kata: Product of the main diagonal of a square matrix.
URL: https://www.codewars.com/kata/551204b7509063d9ba000b45/python
"""


def main_diagonal_product(mat):
    return reduce(lambda x, y: x*y, [mat[x][x] for x in xrange(len(mat))])

