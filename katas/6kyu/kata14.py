"""
Codewars 6 kyu kata: Vowel Count
URL: https://www.codewars.com/kata/54ff3102c1bad923760001f3/python
"""


def getCount(inputStr):
    return len([x for x in inputStr if x in 'aeiou'])

