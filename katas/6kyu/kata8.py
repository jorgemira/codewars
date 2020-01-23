"""
Codewars 6 kyu kata: Easy Diagonal
URL: https://www.codewars.com/kata/559b8e46fa060b2c6a0000bf/python
"""


from math import factorial as f

def diagonal(n, p):
    return f(n + 1) // (f(n - p) * f(p + 1))

