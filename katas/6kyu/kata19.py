"""
Codewars 6 kyu kata: Reverse polish notation calculator
URL: https://www.codewars.com/kata/52f78966747862fc9a0009ae/python
"""


CASE = {'+': lambda x, y: y + x, '-': lambda x, y: y - x, '*': lambda x, y: y * x, '/': lambda x, y: y / x}
def calc(expr):
    rpn = lambda l, v: [CASE[v](l[0], l[1])] + l[2:] if v in CASE else [float(v)] + l
    return reduce(rpn, expr.split(), [0])[0]

