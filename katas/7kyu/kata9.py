"""
Codewars 7 kyu kata: Rigged Dice
URL: https://www.codewars.com/kata/573acc8cffc3d13f61000533/python
"""


from random import randint
def throw_rigged():
    n = randint(0,999)
    if n < 220 :
        return 6
    else:
        return randint(1,5)

