"""
Codewars 6 kyu kata: The fusc function -- Part 1
URL: https://www.codewars.com/kata/570409d3d80ec699af001bf9/python
"""


def fusc(n):
    if n < 2:
        return n
    return fusc(n / 2) + (fusc(n / 2 + 1) if n % 2 else 0)

