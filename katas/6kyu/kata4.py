"""
Codewars 6 kyu kata: Alphabet war
URL: https://www.codewars.com/kata/59377c53e66267c8f6000027/python
"""


def alphabet_war(fight):
    vals = {'w': 4, 'p': 3, 'b': 2, 's': 1, 'm': -4, 'q': -3, 'd': -2, 'z': -1}
    r = sum(vals.get(v, 0) for v in fight)
    if r < 0:
        return "Right side wins!"
    elif r > 0:
        return "Left side wins!"
    else:
        return "Let's fight again!"

