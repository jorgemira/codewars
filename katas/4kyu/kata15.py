"""
Codewars 4 kyu kata: Number of trailing zeros of N!
URL: https://www.codewars.com/kata/52f787eb172a8b4ae1000a34/python
"""


def zeros(n):
    return sum(n / 5**x for x in xrange(1, 15))

