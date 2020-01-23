"""
Codewars 3 kyu kata: Alphabetic Anagrams
URL: https://www.codewars.com/kata/53e57dada0cb0400ba000688/python
"""


from collections import Counter
from operator import mul

def combinations(c):
    f = lambda x: reduce(mul, xrange(1, x + 1))
    return f(sum(c.values())) / reduce(mul, (f(i) for i in c.values()))

def listPosition(word, c=None):
    if not word:
        return 1

    if not c:
        c = Counter(word)

    acc = 0

    for l in sorted(c):
        if l == word[0]:
            return acc + listPosition(word[1:], c - Counter([word[:1]]))

        acc += combinations(c - Counter(l))

