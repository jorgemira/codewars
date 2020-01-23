"""
Codewars 7 kyu kata: Find the anonymous function
URL: https://www.codewars.com/kata/55a12bb8f0fac1ba340000aa/python
"""


def find_function(func,arr):
    for f in func:
        if hasattr(f, '__call__'):
            return filter(f, arr)

