"""
Codewars 5 kyu kata: Square into Squares. Protect trees!
URL: https://www.codewars.com/kata/54eb33e5bc1a25440d000891/python
"""


def squares(sq, n):
    for i in reversed(xrange(n)):
        i2 = i**2
        if sq == i2:
            return [i]
        elif sq > i2:
            try:
                return squares(sq - i2, i) + [i]
            except TypeError:
                pass
    
    return None

def decompose(n):
    return squares(n**2, n)

