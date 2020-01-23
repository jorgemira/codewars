"""
Codewars 4 kyu kata: Base64 Encoding
URL: https://www.codewars.com/kata/5270f22f862516c686000161/python
"""


ALPH = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'


def to_base_64(string):
    result = []

    for s in (string[x:x + 3] for x in xrange(0, len(string), 3)):
        tmp = ''.join(('0' * (8 - len(bin(ord(c))[2:]))) + bin(ord(c))[2:] for c in s)
        tmp += '0' * (32 - len(tmp))
        result += [ALPH[int(tmp[b:b + 6], 2)] for b in xrange(0, 24, 6)]

    lasts = (3 - len(string)) % 3
    if lasts:
        result[-lasts:] = [''] * lasts

    return ''.join(result)


def from_base_64(string):
    result = []
    
    for s in (string[x:x + 4] for x in xrange(0, len(string), 4)):
        tmp = ''.join(('0' * (6 - len(bin(ALPH.index(c))[2:]))) + bin(ALPH.index(c))[2:] for c in s)
        result += [chr(int(tmp[b:b + 8], 2)) for b in xrange(0, 24, 8) if tmp[b:b + 8] and int(tmp[b:b + 8])]

    return ''.join(result)

