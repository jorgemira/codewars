"""
Codewars 4 kyu kata: Largest Numeric Palindrome
URL: https://www.codewars.com/kata/556f4a5baa4ea7afa1000046/python
"""


from itertools import combinations
from collections import Counter

def palyndrom(n):
    c = Counter(str(n))
    max_odd = max(c, key=lambda x: int(x) if c[x] % 2 else -1) if any(x for x in c if c[x] % 2) else ''
    c -= Counter(max_odd)
    if '0' in c and c['0'] > 1 and len([x for x in c if c[x] > 1]) == 1:
        del c['0']
    result = ''.join(sorted((x * (c[x] / 2) for x in c if c[x] > 1), key=lambda x: int(x[0])))
    return int(''.join(result[::-1] + str(max_odd) + result))


def numeric_palindrome(*args):
    vals = set(reduce(lambda x, y: x*y, subset) for s in range(2, len(args)+1) for subset in combinations(args, s))
    return max(palyndrom(n) for n in vals)

