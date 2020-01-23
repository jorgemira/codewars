"""
Codewars 5 kyu kata: Integers: Recreation One
URL: https://www.codewars.com/kata/55aa075506463dac6600010d/python
"""


from math import sqrt

def list_squared(m, n):
    r = []
    for a in range(m, n + 1):
        s = sum(i ** 2 + (0 if i**2 == a else (a // i) ** 2)
                for i in range(1, int(sqrt(a)) + 1) if not a % i)
        if int(sqrt(s)) ** 2 == s:
            r.append([a, s])
    return r

