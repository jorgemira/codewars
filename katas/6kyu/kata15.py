"""
Codewars 6 kyu kata: Coding with Squared Strings
URL: https://www.codewars.com/kata/56fcc393c5957c666900024d/python
"""


from math import sqrt, ceil
from itertools import chain


def code(s):
    if not len(s):
        return ""
    n = ceil(sqrt(len(s)))
    s += (n ** 2 - len(s)) * '\v'
    square = [s[i:i + n] for i in range(0, len(s), n)]
    return '\n'.join(''.join(i) for i in zip(*square[::-1]))


def decode(s):
    if not len(s):
        return ""
    return ''.join(chain.from_iterable(reversed(list(zip(*s.split('\n')))))).replace('\v', '')

