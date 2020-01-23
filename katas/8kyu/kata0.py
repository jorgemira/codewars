"""
Codewars 8 kyu kata: Find the missing term in an Arithmetic Progression
URL: https://www.codewars.com/kata/52de553ebb55d1fca3000371/python
"""


def find_missing(seq):
    return (set(xrange(seq[0], seq[-1], (seq[-1] - seq[0]) / len(seq))) - set(seq)).pop()

