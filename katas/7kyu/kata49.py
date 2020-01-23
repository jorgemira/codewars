"""
Codewars 7 kyu kata: Complete The Pattern #7 - Cyclical Permutation
URL: https://www.codewars.com/kata/557592fcdfc2220bed000042/python
"""


def pattern(n):
    if n <= 0:
        return ""

    tmp = range(1,n+1)
    strs = []

    for i in xrange(n):
        strs.append(''.join([str(x) for x in tmp]))
        tmp = tmp[1:] + tmp[0:1]


    return '\n'.join(strs)

