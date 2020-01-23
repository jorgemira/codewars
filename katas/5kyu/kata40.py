"""
Codewars 5 kyu kata: Find The Minimum Number Divisible by Integers of an Array I
URL: https://www.codewars.com/kata/56f245a7e40b70f0e3000130/python
"""


from fractions import gcd

def min_special_mult(arr):

    valid, invalid = set(), []

    for a in arr:
        try:
            valid.add(abs(int(a)))
        except ValueError:
            invalid.append(a)
        except TypeError:
            pass

    if invalid:
        if len(invalid) == 1:
            return "There is 1 invalid entry: {}".format(invalid[0])
        else:
            items = ', '.join(["'{}'".format(i) for i in invalid])
            return "There are {} invalid entries: [{}]".format(len(invalid), items)

    lcm = lambda x, y: x * y / gcd(x, y)

    return reduce(lcm, valid)

