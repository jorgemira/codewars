"""
Codewars 5 kyu kata: Caesar Cipher Helper
URL: https://www.codewars.com/kata/526d42b6526963598d0004db/python
"""


from string import ascii_uppercase as ALPH


class CaesarCipher(object):
    def __init__(self, shift):
        self.shift = shift

    def encode(self, str):
        return ''.join(ALPH[(ALPH.index(c) + self.shift) % len(ALPH)] if c in ALPH else c for c in str.upper())

    def decode(self, str):
        return ''.join(ALPH[ALPH.index(c) - self.shift] if c in ALPH else c for c in str.upper())

