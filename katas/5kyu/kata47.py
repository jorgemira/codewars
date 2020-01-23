"""
Codewars 5 kyu kata: C.Wars
URL: https://www.codewars.com/kata/55968ab32cf633c3f8000008/python
"""


def initials(name):
    names = name.split()
    last = names.pop()
    return ''.join(w[0].upper() + '.' for w in names) + last.capitalize()

