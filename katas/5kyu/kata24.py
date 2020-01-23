"""
Codewars 5 kyu kata: Product of consecutive Fib numbers
URL: https://www.codewars.com/kata/5541f58a944b85ce6d00006a/python
"""


def productFib(prod):
    a, b = 0, 1
    while True:
        a, b = b, a + b
        if a * b >= prod:
            return [a, b, a * b == prod]

