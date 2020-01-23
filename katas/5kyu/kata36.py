"""
Codewars 5 kyu kata: Going to zero or to infinity?
URL: https://www.codewars.com/kata/55a29405bc7d2efaff00007c/python
"""


def going(n):
    acc, tot = 1.0, 1

    for i in reversed(xrange(2, n+1)):
        acc *= i
        tmp = 1 / acc
        if not round(tmp, 7):
            break
        tot += tmp
    
    return float(str(tot)[:8])

