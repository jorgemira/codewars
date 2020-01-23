"""
Codewars 5 kyu kata: Weight for weight
URL: https://www.codewars.com/kata/55c6126177c9441a570000cc/python
"""


def order_weight(strng):
    return ' '.join(sorted(strng.split(' '), key=lambda x: (sum(int(i) for i in x), x)))

