"""
Codewars 6 kyu kata: Base Conversion
URL: https://www.codewars.com/kata/526a569ca578d7e6e300034e/python
"""


def convert(input, source, target):
    num = sum(len(source)**i * source.index(n) for i, n in enumerate(input[::-1]))
    tmp = []
    while num:
        tmp.append(target[num % len(target)])
        num /= len(target)
    return ''.join(tmp[::-1]) if tmp else target[0]

