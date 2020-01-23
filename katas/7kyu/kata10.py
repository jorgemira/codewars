"""
Codewars 7 kyu kata: Vigenère Autokey Cipher Helper
URL: https://www.codewars.com/kata/52d2e2be94d26fc622000735/python
"""


class VigenereAutokeyCipher:

    def __init__(self, key, abc):
        self.key = key
        self.abc = abc

    def encode(self, text):

        coder = self.key + ''.join(l for l in text if l in self.abc)
        
        for i in xrange(len(text)):
            if text[i] not in self.abc:
                coder = coder[:i] + text[i] + coder[i:]

        coder = coder[:len(text)]

        return ''.join(self.abc [(self.abc.index(text[i]) + self.abc.index(coder[i])) % len(self.abc)] if text[i] in self.abc else text[i] for i in xrange(len(text)))

    def decode(self, text):
        coder = self.key
        out = ''
        
        for i in xrange(len(text)):
            if text[i] not in self.abc:
                coder = coder[:i] + text[i] + coder[i:]
                c = text[i]
            else:
                c = self.abc[(self.abc.index(text[i]) - self.abc.index(coder[i])) % len(self.abc)]
                coder += c
            out += c
            
        return out

