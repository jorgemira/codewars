"""
Codewars 6 kyu kata: Weird prime generator
URL: https://www.codewars.com/kata/562b384167350ac93b00010c/python
"""


from fractions import gcd


def an():
    r, i = 7, 2

    while True:
        yield r
        r = r + gcd(i, r)
        i += 1


def gn():
    r, i, a = 6, 0, an()

    while True:
        i = next(a)
        yield i - r
        r = i


def count_ones(n):
    g = gn()

    return len([None for _ in xrange(n) if next(g) == 1])


def p(n):
    tmp, g = set(), gn()

    while len(tmp) <= n:
        tmp.add(next(g))

    tmp.discard(1)
    
    return tmp


def max_pn(n):
    return max(p(n))


def an_over(n):
    return [3] * n


def an_over_average(n):
    return 3

