"""
Codewars 5 kyu kata: The Millionth Fibonacci Kata
URL: https://www.codewars.com/kata/53d40c1e2f13e331fc000c26/python
"""


def _fib(n):
    if n == 0:
        return (0, 1)
    else:
        a, b = _fib(n / 2)
        c = a * (b * 2 - a)
        d = a * a + b * b
        if n % 2 == 0:
            return (c, d)
        else:
            return (d, c + d)

def fib(n):
    r = _fib(abs(n))[0]
    return -r if n < 0 and not n % 2 else r

