"""
Codewars 6 kyu kata: IQ Test
URL: https://www.codewars.com/kata/552c028c030765286c00007d/python
"""


def iq_test(numbers):
    nums = [ int(x) for x in numbers.split(' ')]
    
    odds = [x for x in nums if x % 2]
    evens = [x for x in nums if not x % 2]
    
    return nums.index(odds[0] if len(odds) == 1 else evens[0]) + 1

