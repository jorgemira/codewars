"""
Codewars 5 kyu kata: Character Frequency
URL: https://www.codewars.com/kata/548ef5b7f33a646ea50000b2/python
"""


def char_freq(message):
    return {x : message.count(x) for x in message}

