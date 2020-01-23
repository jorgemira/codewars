"""
Codewars 8 kyu kata: Credit Card Mask
URL: https://www.codewars.com/kata/5412509bd436bd33920011bc/python
"""


def maskify(cc):
    return cc if len(cc) < 5 else ''.join(['#'] * (len(cc)-4)) + cc[-4:]

