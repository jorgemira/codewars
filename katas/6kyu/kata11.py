"""
Codewars 6 kyu kata: Following the Paths of Numbers Through Prime Factorization
URL: https://www.codewars.com/kata/58f301633f5066830c000092/python
"""


from functools import reduce
from operator import mul
from itertools import combinations


def get_num(arr):
    n = reduce(mul, arr, 1)
    divs = {reduce(mul, factors, 1) for i in range(1, len(arr))
            for factors in combinations(arr, i)}
    return [n, len(divs) + 1, min(divs), max(divs)]

