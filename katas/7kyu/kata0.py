"""
Codewars 7 kyu kata: Alphabet war - airstrike - letters massacre
URL: https://www.codewars.com/kata/5938f5b606c3033f4700015a/python
"""


def alphabet_war(fight):
    fight = list(fight)
    for i, x in enumerate(fight):
        if x == '*':
            if i > 0 and fight[i -1] != '*':
                fight[i - 1] = '_'
            if i < len(fight) - 1 and fight[i + 1] != '*':
                fight[i + 1] = '_'
    vals = {'w': 4, 'p': 3, 'b': 2, 's': 1, 'm': -4, 'q': -3, 'd': -2, 'z': -1}
    r = sum(vals.get(v, 0) for v in fight)
    if r < 0:
        return "Right side wins!"
    elif r > 0:
        return "Left side wins!"
    else:
        return "Let's fight again!"

