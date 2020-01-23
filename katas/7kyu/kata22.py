"""
Codewars 7 kyu kata: Dropcaps
URL: https://www.codewars.com/kata/559e5b717dd758a3eb00005a/python
"""


def drop_cap(str_):
    return ' '.join([x.capitalize() if len(x) > 2 else x for x in str_.split(' ')])

