"""
Codewars 7 kyu kata: Jaden Casing Strings
URL: https://www.codewars.com/kata/5390bac347d09b7da40006f6/python
"""


def toJadenCase(string):
    return ' '.join(s.capitalize() for s in string.split())

