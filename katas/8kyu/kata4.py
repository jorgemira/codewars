"""
Codewars 8 kyu kata: Where is Vasya?
URL: https://www.codewars.com/kata/554754ac9d8ac3be120000b2/python
"""


def where_is_he(p, bef, aft):
    return min(p - bef, aft + 1)

