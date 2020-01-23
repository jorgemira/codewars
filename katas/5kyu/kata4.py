"""
Codewars 5 kyu kata: Square sums (simple)
URL: https://www.codewars.com/kata/5a6b24d4e626c59d5b000066/python
"""


def square_sums_row(n):
    mem = {}

    for i in range(1, n + 1):
        mem[i] = []
        for j in range(1, n + 1):
            if j != i and int((i + j) ** .5) ** 2 == i + j:
                mem[i].append(j)

    return _bt(mem, n, [], range(1, n + 1))


def _bt(m, n, r, op):
    if len(r) == n:
        return r

    for x in op:
        if x not in r:
            r.append(x)
            a = _bt(m, n, r, m[x])
            if a:
                return a
            r.pop()

    return False

