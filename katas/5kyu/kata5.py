"""
Codewars 5 kyu kata: Roof Replacement
URL: https://www.codewars.com/kata/57d15a03264276aaf000007f/python
"""


def roof_fix(f,r):
    return not any(a != ' ' and b in '/\\' for a, b in zip(f, r))

