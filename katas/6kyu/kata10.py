"""
Codewars 6 kyu kata: Irreducible Sum of Rationals
URL: https://www.codewars.com/kata/5517fcb0236c8826940003c9/python
"""


from fractions import Fraction


def sum_fracts(lst):
    if not lst:
        return None

    f = sum(Fraction(*f) for f in lst)
    n, d = f.numerator, f.denominator
    return [n, d] if n % d else n / d

