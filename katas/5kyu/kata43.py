"""
Codewars 5 kyu kata: Gap in Primes
URL: https://www.codewars.com/kata/561e9c843a2ef5a40c0000a4/python
"""


from math import sqrt


def memo(func):
    cache = {}
    def wrap(arg):
        if arg not in cache:
            cache[arg] = func(arg)
        return cache[arg]
    return wrap


@memo
def is_prime(num):
    if num < 2:
        return False
    if num == 2:
        return True
    if not num % 2:
        return False

    mid = int(sqrt(num)) + 1

    for count in xrange(3, mid, 2):
        if not num % count:
            return False

    return True


def gap(g, m, n):
    for i in xrange(m, n - g + 1):
        if is_prime(i) and is_prime(i + g):
            if not any(is_prime(i) for i in xrange(i + 1, i + g)):
                return [i, i + g]
    return None

