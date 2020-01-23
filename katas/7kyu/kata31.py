"""
Codewars 7 kyu kata: Are You Playing Banjo?
URL: https://www.codewars.com/kata/53af2b8861023f1d88000832/python
"""


def areYouPlayingBanjo(name):
    return name + (' plays' if name.upper().startswith('R') else ' does not play') + ' banjo'

