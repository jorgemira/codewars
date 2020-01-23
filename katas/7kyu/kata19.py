"""
Codewars 7 kyu kata: Name Shuffler
URL: https://www.codewars.com/kata/559ac78160f0be07c200005a/python
"""


def name_shuffler(str_):
    return ' '.join(str_.split()[::-1])

