"""
Codewars 8 kyu kata: Next bigger number with the same digits
URL: https://www.codewars.com/kata/55983863da40caa2c900004e/python
"""


def next_bigger(n):
    max_n = int(''.join(reversed(sorted(str(n)))))
    if n == max_n:
        return -1
    while True:
        n+=1
        if max_n == int(''.join(reversed(sorted(str(n))))):
            return n

