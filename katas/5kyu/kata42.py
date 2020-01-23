"""
Codewars 5 kyu kata: First n Prime Numbers
URL: https://www.codewars.com/kata/535bfa2ccdbf509be8000113/python
"""


from math import sqrt


def memo(func):
    cache = {}
    def wrap(arg):
        if arg not in cache:
            cache[arg] = func(arg)
        return cache[arg]
    return wrap


class Primes:
    @staticmethod
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


    @staticmethod
    def first(n):
        primes = []
        i = 1
        while len(primes) < n:
            if Primes.is_prime(i):
                primes.append(i)
            i += 1
        return primes

