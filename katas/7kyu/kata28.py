"""
Codewars 7 kyu kata: X marks the spot!
URL: https://www.codewars.com/kata/55cc20eb943f1d8b11000045/python
"""


def x(n):
    result = []

    for i in xrange(n):
        line = [0] * n
        line[i], line[-(i+1)] = 1,1
        result.append(line)

    return result

