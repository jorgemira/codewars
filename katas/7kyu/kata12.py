"""
Codewars 7 kyu kata: How Much?
URL: https://www.codewars.com/kata/55b4d87a3766d9873a0000d4/python
"""


def howmuch(m, n):
    bottom, top = min(n, m), max(n, m)
    result = []
    
    for i in xrange(bottom, top+1):
        if not (i - 1) % 9 and not (i - 2) % 7:
            b, c = ((i-2)/7), ((i-1)/9)
            result.append(["M: %s" % i, "B: %s" % b, "C: %s" % c])
            
    return result

