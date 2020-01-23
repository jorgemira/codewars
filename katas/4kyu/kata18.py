"""
Codewars 4 kyu kata: Magnet particules in boxes
URL: https://www.codewars.com/kata/56c04261c3fcf33f2d000534/python
"""


def doubles(maxk, maxn):
    v = lambda k, n: 1. / (k * (n + 1) ** (2 * k)) if len(str((n + 1) ** (2 * k))) < 10 else 0    
    result = 0
    
    for k in xrange(maxk):
        for n in xrange(maxn):
            tmp = v(k+1, n+1)
            if tmp:
                result += tmp
            else:
                break
    
    return result

