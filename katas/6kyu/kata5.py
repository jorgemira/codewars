"""
Codewars 6 kyu kata: Integer depth
URL: https://www.codewars.com/kata/59b401e24f98a813f9000026/python
"""


def compute_depth(n):
    s = set()
    i = 0
    
    while len(s) < 10:
        i += 1
        s.update(str(n*i))
    
    return i

