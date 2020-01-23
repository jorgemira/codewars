"""
Codewars 5 kyu kata: Matrix Trace
URL: https://www.codewars.com/kata/55208f16ecb433c5c90001d2/python
"""


def trace(matrix):
    m = len(matrix)
    if not m or any(len(row) != m for row in matrix):
        return None
    return sum(matrix[i][i] for i in range(m))

