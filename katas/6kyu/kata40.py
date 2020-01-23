"""
Codewars 6 kyu kata: Primes in numbers
URL: https://www.codewars.com/kata/54d512e62a5e54c96200019e/python
"""


from math import sqrt

def primeFactors(n):
    tmp = {}
    count = 2
    limit = sqrt(n)

    while n != 1 or count < limit:
        if not n % count:
            tmp[count] = 0
            while not n % count:
                n /= count
                tmp[count] += 1
            limit = sqrt(n)
        count += 1

    return ''.join("(%i%s)" % (x, "**%s"%tmp[x] if tmp[x] > 1 else "") for x in sorted(tmp))

