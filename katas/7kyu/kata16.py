"""
Codewars 7 kyu kata: Is n divisible by (...)?
URL: https://www.codewars.com/kata/558ee8415872565824000007/python
"""


def is_divisible(n, *rest):
    return all(not n % i for i in rest)

