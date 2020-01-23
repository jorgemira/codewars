"""
Codewars 5 kyu kata: Last digit of a large number
URL: https://www.codewars.com/kata/5511b2f550906349a70004e1/python
"""


def last_digit(n1, n2):
    cache = [[0], [1], [6, 2, 4, 8], [1, 3, 9, 7], [6, 4], [5], [6], [1, 7, 9, 3], [6, 8, 4, 2], [1, 9]]
    return cache[n1 % 10][n2 % len(cache[n1 % 10])] if n2 else 1

