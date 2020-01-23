"""
Codewars 6 kyu kata: first character that repeats
URL: https://www.codewars.com/kata/54f9f4d7c41722304e000bbb/python
"""


def first_dup(s):
    for i, c in enumerate(s):
        if c in s[i + 1:]:
            return c
    return None

