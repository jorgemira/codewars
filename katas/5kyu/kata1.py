"""
Codewars 5 kyu kata: String incrementer
URL: https://www.codewars.com/kata/54a91a4883a7de5d7800009c/python
"""


import re


def incr(match):
    m = match.group()
    return str(int(m) + 1).zfill(len(m)) if m else '1'


def increment_string(strng):
    return re.sub(r'([0-9]*)$', incr, strng)

