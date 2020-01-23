"""
Codewars 7 kyu kata: Complete The Pattern #16
URL: https://www.codewars.com/kata/55ae997d1c40a199e6000018/python
"""


def pattern(n):

    if n <= -50 or n > 150:
        return ''

    result = []

    for i in xrange(n):
        tmp = ''.join([str((n-j) % 10) for j in xrange(0, i+1)])
        tmp += str((n-i) % 10) * (n - i - 1)
        result.append(tmp)

    return '\n'.join(result)

