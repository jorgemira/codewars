"""
Codewars 5 kyu kata: Sum of Multiples
URL: https://www.codewars.com/kata/57241e0f440cd279b5000829/python
"""


def sum_mul(n, m):
    return sum(i for i in xrange(n,m) if not i % n) if n > 0 and m > 0 else 'INVALID'

