"""
Codewars 8 kyu kata: Playing on a chessboard
URL: https://www.codewars.com/kata/55ab4f980f2d576c070000f4/python
"""


def game(n):
    return [n ** 2, 2] if n % 2 else [n * (n / 2)]

