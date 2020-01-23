"""
Codewars 7 kyu kata: Persistent Bugger.
URL: https://www.codewars.com/kata/55bf01e5a717a0d57e0000ec/python
"""


from functools import reduce
from operator import mul


def persistence(n):
    return 1 + persistence(reduce(mul, [int(x) for x in str(n)], 1)) if n > 9 else 0

