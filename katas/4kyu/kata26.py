"""
Codewars 4 kyu kata: Explosive Sum
URL: https://www.codewars.com/kata/52ec24228a515e620b0005ef/python
"""


import functools

def memoize(obj):
    cache = obj.cache = {}

    @functools.wraps(obj)
    def memoizer(*args, **kwargs):
        if args not in cache:
            cache[args] = obj(*args, **kwargs)
        return cache[args]
    return memoizer

@memoize
def num_ways(num, parts):
    ways = 0
    if num:
        if parts:
            max_part = parts[0]
            if num >= max_part:
                ways += num_ways(num - max_part, parts)
            ways += num_ways(num, parts[1:])
        return ways
    else:
        return 1

def exp_sum(n):
    if n < 0:
        return 0
    return num_ways(n, tuple(range(1,n+1)[::-1]))

