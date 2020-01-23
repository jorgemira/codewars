"""
Codewars 7 kyu kata: Alphabetize a list by the nth character
URL: https://www.codewars.com/kata/54eea36b7f914221eb000e2f/python
"""


def sort_it(list_, n):
    return ', '.join(sorted(list_.split(', '), key=lambda x: x[n - 1]))

