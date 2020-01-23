"""
Codewars 6 kyu kata: Casino chips
URL: https://www.codewars.com/kata/5e0b72d2d772160011133654/python
"""


def solve(arr):
    a, b, c = sorted(arr)
    return a + b if a + b < c else sum(arr) // 2

