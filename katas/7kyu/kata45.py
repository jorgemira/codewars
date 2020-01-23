"""
Codewars 7 kyu kata: Filter the number
URL: https://www.codewars.com/kata/55b051fac50a3292a9000025/python
"""


def filter_string(string):
    return int(''.join(x for x in string if x in '0123456789'))

