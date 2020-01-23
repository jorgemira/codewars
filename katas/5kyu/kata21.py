"""
Codewars 5 kyu kata: Find heavy ball - level: master
URL: https://www.codewars.com/kata/544034f426bc6adda200000e/python
"""


def find_ball(scales):
    left, right = [0, 1, 2], [3, 4, 5]
    w = scales.get_weight(left, right)
    tmp = left if w < 0 else right if w > 0 else [6, 7]
    w = scales.get_weight([tmp[0]], [tmp[1]])
    return tmp[0] if w < 0 else tmp[1] if w > 0 else tmp[2]

