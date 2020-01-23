"""
Codewars 5 kyu kata: What's a Perfect Power anyway?
URL: https://www.codewars.com/kata/54d4c8b08776e4ad92000835/python
"""


def isPP(n):
    for i in xrange(2, int(n ** .5)+1):
        if not n % i:
            count = 0
            tmp = n
            while not tmp % i:
                tmp /= i
                count += 1
            if tmp == 1:
                return [i, count]

    return None

