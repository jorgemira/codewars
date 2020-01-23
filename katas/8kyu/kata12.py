"""
Codewars 8 kyu kata: Convert number to reversed array of digits
URL: https://www.codewars.com/kata/5583090cbe83f4fd8c000051/python
"""


def digitize(n):
    return list(reversed([int(x) for x in str(n)]))

