"""
Codewars 6 kyu kata: Positions Average
URL: https://www.codewars.com/kata/59f4a0acbee84576800000af/python
"""


from itertools import combinations, chain

def pos_average(s):
    equals = list(chain((a == b for s1, s2 in combinations(s.split(', '), 2)
                         for a, b in zip(s1, s2))))
    return (sum(equals) / len(equals)) * 100

