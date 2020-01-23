"""
Codewars 5 kyu kata: Scramblies
URL: https://www.codewars.com/kata/55c04b4cc56a697bb0000048/python
"""


from collections import Counter


def scramble(s1, s2):
    c2 = Counter(s2)
    c2.subtract(Counter(s1))

    return all(c <= 0 for c in c2.values())

