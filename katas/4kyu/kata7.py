"""
Codewars 4 kyu kata: Permutations
URL: https://www.codewars.com/kata/5254ca2719453dcc0b00027d/python
"""


from itertools import permutations as perms

def permutations(string):
    return set([''.join(p) for p in perms(string)])

