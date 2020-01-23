"""
Codewars 7 kyu kata: Where my anagrams at?
URL: https://www.codewars.com/kata/523a86aa4230ebb5420001e1/python
"""


def anagrams(word, words):
    sw = sorted(word)
    return [w for w in words if sw == sorted(w)]

