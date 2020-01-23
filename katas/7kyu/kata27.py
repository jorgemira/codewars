"""
Codewars 7 kyu kata: Failed Filter - Bug Fixing #3
URL: https://www.codewars.com/kata/55c606e6babfc5b2c500007c/python
"""


def filter_numbers(string):
    return "".join(x for x in string if not x in '0123456789')

