"""
Codewars 7 kyu kata: Alternate Square Sum
URL: https://www.codewars.com/kata/559d7951ce5e0da654000073/python
"""


def alternate_sq_sum(arr):
    return sum(v if not i%2 else v**2 for i, v in enumerate(arr))

