"""
Codewars 6 kyu kata: Find The Parity Outlier
URL: https://www.codewars.com/kata/5526fc09a1bbd946250002dc/python
"""


def find_outlier(integers):
    odd = sum(i % 2 for i in integers[:3]) <= 1
    return [x for x in integers if x % 2 == odd][0]

