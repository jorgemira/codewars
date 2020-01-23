"""
Codewars 6 kyu kata: Stop gninnipS My sdroW!
URL: https://www.codewars.com/kata/5264d2b162488dc400000001/python
"""


def spin_words(sentence):
    return ' '.join(w if len(w) < 5 else ''.join(reversed(w)) for w in sentence.split())

