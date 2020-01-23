"""
Codewars 7 kyu kata: Bit Counting
URL: https://www.codewars.com/kata/526571aae218b8ee490006f4/python
"""


def countBits(n):
    return sum(int(x) for x in "{0:b}".format(n))

