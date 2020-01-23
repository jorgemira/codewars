"""
Codewars 7 kyu kata: Highest and Lowest
URL: https://www.codewars.com/kata/554b4ac871d6813a03000035/python
"""


def high_and_low(numbers):
    arr = [int(x) for x in numbers.split(' ')]
    return "{} {}".format(max(arr), min(arr))

