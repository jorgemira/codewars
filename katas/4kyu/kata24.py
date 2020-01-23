"""
Codewars 4 kyu kata: How many consecutive numbers are needed?
URL: https://www.codewars.com/kata/559cc2d2b802a5c94700000c/python
"""


def consecutive(arr):
    return max(arr) - min(arr) - len(arr) + 1 if arr else 0

