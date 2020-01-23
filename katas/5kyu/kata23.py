"""
Codewars 5 kyu kata: Perimeter of squares in a rectangle
URL: https://www.codewars.com/kata/559a28007caad2ac4e000083/python
"""


def perimeter(n):
    a, b = 1, 1
    tmp = 0
    for _ in xrange(n + 1):
        tmp += a
        a, b = b, a + b
    return tmp * 4

