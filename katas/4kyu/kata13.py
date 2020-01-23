"""
Codewars 4 kyu kata: Factorial tail
URL: https://www.codewars.com/kata/55c4eb777e07c13528000021/python
"""


def factors(n, dic=None):
    if dic:
        flist = dic.keys()
    else:
        dic = {}
        flist = xrange(2, n / 2 + 1)

    for i in flist:
        while not n % i:
            dic[i] = dic.get(i, 0) + 1
            n /= i

    return dic


def zeroes(base, number):
    pf = factors(base) or {base: 1}
    acc = {k: 0 for k in pf}
    for i in xrange(2, number + 1):
        acc = factors(i, acc)

    return min(acc.get(k, 0) / pf[k] for k in pf) if pf else 0

