"""
Codewars 4 kyu kata: Hamming Numbers
URL: https://www.codewars.com/kata/526d84b98f428f14a60008da/python
"""


from itertools import islice, chain, tee


def merge(r, s):
    rr = r.next()
    ss = s.next()
    while True:
        if rr < ss:
            yield rr
            rr = r.next()
        else:
            yield ss
            ss = s.next()


def p(n):
    def gen():
        x = n
        while True:
            yield x
            x *= n
    return gen()


def pp(n, s):
    def gen():
        for x in (merge(s, chain([n], (n * y for y in fb)))):
            yield x
    r, fb = tee(gen())
    return r


def hamming(a, b=None):
    if not b:
        b = a + 1
    seq = (chain([1], pp(5, pp(3, p(2)))))
    return list(islice(seq, a - 1, b - 1))[0]

