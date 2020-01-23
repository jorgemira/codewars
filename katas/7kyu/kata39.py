"""
Codewars 7 kyu kata: Grasshopper - Array Mean
URL: https://www.codewars.com/kata/55d277882e139d0b6000005d/python
"""


def find_average(nums):
    return sum(nums) / float(len(nums)) if nums else 0

