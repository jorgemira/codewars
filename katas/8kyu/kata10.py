"""
Codewars 8 kyu kata: Memoized Fibonacci
URL: https://www.codewars.com/kata/529adbf7533b761c560004e5/python
"""


def fibonacci(n):
    if not hasattr(fibonacci, "cache"):
        fibonacci.cache = [0,1]

    try:
        return fibonacci.cache[n]
    except IndexError:
        fibonacci.cache.append(fibonacci(n-1) + fibonacci(n-2))
        return fibonacci.cache[n]

