"""
Codewars 5 kyu kata: Roman Numerals Encoder
URL: https://www.codewars.com/kata/51b62bf6a9c58071c600001b/python
"""


def solution(n):
    nums = [['I', 'X', 'C', 'M'], ['II', 'XX', 'CC', 'MM'], ['III', 'XXX', 'CCC', 'MMM'], ['IV', 'XL', 'CD'],
            ['V', 'L', 'D'], ['VI', 'LX', 'DC'], ['VII', 'LXX', 'DCC'], ['VIII', 'LXXX', 'DCCC'], ['IX', 'XC', 'CM']]
    return ''.join([nums[int(x) - 1][i] for i, x in zip(reversed(xrange(len(str(n)))), str(n)) if int(x)])

