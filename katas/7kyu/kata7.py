"""
Codewars 7 kyu kata: The unknown but known variables: Addition
URL: https://www.codewars.com/kata/5716955a794d3013d00013f9/python
"""


def the_var(the_variables):
    return sum(ord(v) - 96 for v in the_variables if 97 <= ord(v) <= 122)

