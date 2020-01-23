"""
Codewars 4 kyu kata: Morse Encoding
URL: https://www.codewars.com/kata/536602df5d0266e7b0000d31/python
"""


class Morse:
    @classmethod
    def encode(cls, message):
        txt = cls.sep.join(cls.alpha[c] for c in message)
        txt += '0' * (cls.wlen - (len(txt) % cls.wlen))  # Add padding
        return [int(txt[i:cls.wlen + i], 2) - ((1 << cls.wlen) if txt[i: i + 1] == '1' else 0) for i in xrange(0, len(txt), cls.wlen)]

    @classmethod
    def decode(cls, array):
        txt = ''.join(bin(n + (1 << cls.wlen))[2 + (1 if n > 0 else 0):] for n in array)
        while txt[-1] == '0':  # Remove padding
            txt = txt[:-1]
        return ' '.join(''.join(cls.rev_alpha[c] for c in word.split(cls.sep)) for word in txt.split(cls.space))

    wlen = 32
    sep = '000'
    alpha = {'A': '10111', 'B': '111010101', 'C': '11101011101', 'D': '1110101', 'E': '1', 'F': '101011101',
             'G': '111011101', 'H': '1010101', 'I': '101', 'J': '1011101110111', 'K': '111010111', 'L': '101110101',
             'M': '1110111', 'N': '11101', 'O': '11101110111', 'P': '10111011101', 'Q': '1110111010111', 'R': '1011101',
             'S': '10101', 'T': '111', 'U': '1010111', 'V': '101010111', 'W': '101110111', 'X': '11101010111',
             'Y': '1110101110111', 'Z': '11101110101', '0': '1110111011101110111', '1': '10111011101110111',
             '2': '101011101110111', '3': '1010101110111', '4': '10101010111', '5': '101010101', '6': '11101010101',
             '7': '1110111010101', '8': '111011101110101', '9': '11101110111011101', '.': '10111010111010111',
             ',': '1110111010101110111', '?': '101011101110101', "'": '1011101110111011101', '!': '1110101110101110111',
             '/': '1110101011101', '(': '111010111011101', ')': '1110101110111010111', '&': '10111010101',
             ':': '11101110111010101', ';': '11101011101011101', '=': '1110101010111', '+': '1011101011101',
             '-': '111010101010111', '_': '10101110111010111', '"': '101110101011101', '$': '10101011101010111',
             '@': '10111011101011101', ' ': '0'}
    space = ''.join([sep, alpha[' '], sep])
    rev_alpha = dict((v, k) for k, v in alpha.iteritems())

