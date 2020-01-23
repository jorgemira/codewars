"""
Codewars 5 kyu kata: Triangle of Multiples (Easy One)
URL: https://www.codewars.com/kata/58ecc0a8342ee5e920000115/python
"""


def mult_triangle(n):
    all = sum((x + 1) ** 3 for x in range(n))
    odds = sum(i ** 2 + sum(2 * i * j for j in range(1, i, 2))
               for i in range(1, n + 1, 2))
    return [all, all - odds, odds]

