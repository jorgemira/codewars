"""
Codewars 6 kyu kata: Return String As Sorted Blocks
URL: https://www.codewars.com/kata/5e0f6a3a2964c800238ca87d/python
"""


def blocks(s):
    groups = [[]]
    order = lambda x: "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789".find(x)

    for l in s:
        for g in groups:
            if l not in g:
                g.append(l)
                break
        else:
            groups.append([l])

    return '-'.join(''.join(sorted(g, key=order)) for g in groups)

