"""
Codewars 4 kyu kata: Sum by Factors
URL: https://www.codewars.com/kata/54d496788776e49e6b00052f/python
"""


from math import sqrt

def prime_factors(num):
    '''Return a list with the prime factors of num'''

    result = []
    count = 2
    limit = sqrt(num)

    while num != 1 or count < limit:
        if not num % count:
            result.append(count)
            while not num % count:
                num /= count
            limit = sqrt(num)
        count += 1

    return result

def sum_for_list(lst):
    tmp = {}
    for n in lst:
        for i in prime_factors(abs(n)):
            try:
                tmp[i] += n
            except KeyError:
                tmp[i] = n
    return [[x, tmp[x]] for x in sorted(tmp)]

