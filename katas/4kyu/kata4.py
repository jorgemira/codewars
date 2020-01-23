"""
Codewars 4 kyu kata: Roman Numerals Decoder
URL: https://www.codewars.com/kata/51b6249c4612257ac0000005/python
"""


NUMS = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

def solution(roman):
    return sum(-NUMS[n] if i < len(roman) - 1 and NUMS[roman[i + 1]] > NUMS[n] else NUMS[n] for i, n in enumerate(roman))

