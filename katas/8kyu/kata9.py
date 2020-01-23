"""
Codewars 8 kyu kata: Figurate Numbers #2 - Pronic Number
URL: https://www.codewars.com/kata/55b1e5c4cbe09e46b3000034/python
"""


def is_pronic(n):
    return ((((1 + 4 * n) ** 0.5) - 1) / 2).is_integer() if n >= 0 else False

