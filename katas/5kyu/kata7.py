"""
Codewars 5 kyu kata: Mumbling
URL: https://www.codewars.com/kata/5667e8f4e3f572a8f2000039/python
"""


def accum(s):
    return '-'.join((i * l).capitalize() for l, i in enumerate(s, 1))

