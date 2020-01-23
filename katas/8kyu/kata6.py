"""
Codewars 8 kyu kata: Every archer has its arrows
URL: https://www.codewars.com/kata/559f89598c0d6c9b31000125/python
"""


def archers_ready(archers):
    return bool(archers) and all(a >= 5 for a in archers)

