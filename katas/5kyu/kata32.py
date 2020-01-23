"""
Codewars 5 kyu kata: Decimal to Factorial and Back
URL: https://www.codewars.com/kata/54e320dcebe1e583250008fd/python
"""


cache = []
for i in xrange(36):
    cache.append(cache[-1] * i if i else 1)

def factString2Dec(num):
    return sum((ord(x) - 48 if ord(x) < 65 else ord(x) - 55) * cache[i] for i, x in enumerate(reversed(num)))

def dec2FactString(nb):
    _to_char = lambda x: chr(x + 48) if x < 10 else chr(x + 55)
    res = ''
    
    for i in reversed(xrange(36)):
        res += _to_char(nb / cache[i])
        nb %= cache[i]
    
    while res.startswith('0'):
        res = res[1:]

    return res

