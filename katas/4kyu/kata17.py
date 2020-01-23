"""
Codewars 4 kyu kata: Strings Mix
URL: https://www.codewars.com/kata/5629db57620258aa9d000014/python
"""


from string import ascii_lowercase
from operator import itemgetter

def mix(s1, s2):
    f = lambda x: {l: x.count(l) for l in ascii_lowercase if x.count(l) > 1}
    d1 = f(s1)
    d2 = f(s2)
    l = []

    for i in set(d1.keys() + d2.keys()):
        if d1.get(i, 0) > d2.get(i, 0):
            l.append((d1.get(i, 0), '1', i))
        elif d1.get(i, 0) < d2.get(i, 0):
            l.append((d2.get(i, 0), '2', i))
        else:
            l.append((d1.get(i, 0), '=', i))

    l.sort(key=itemgetter(2))
    l.sort(key=itemgetter(1))
    l.sort(key=itemgetter(0), reverse=True)

    return '/'.join(i[1]+":"+i[2]*i[0] for i in l)

