"""
Codewars 7 kyu kata: Find the odd int
URL: https://www.codewars.com/kata/54da5a58ea159efa38000836/python
"""


from collections import Counter


def find_it(seq):
    return [k for k, v in Counter(seq).items() if v % 2][0]

