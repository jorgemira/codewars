"""
Codewars 4 kyu kata: Ticker
URL: https://www.codewars.com/kata/5a959662373c2e761d000183/python
"""


def ticker(text, width, tick):
    t = ' ' * width + text
    return (t[tick % (len(text) + width):] + t[0: tick % (len(text) + width)])[:width]

