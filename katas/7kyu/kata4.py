"""
Codewars 7 kyu kata: Getting along with Integer Partitions
URL: https://www.codewars.com/kata/55cf3b567fc0e02b0b00000b/python
"""


def range_(n):
    return n[-1] - 1


def avg(n):
    return sum(n) / float(len(n))


def median(lst):
    mid = (len(lst) - 1) / 2
    return (lst[mid] + lst[mid + (0 if len(lst) % 2 else 1)]) / 2.0


def partitions(n, lst=None):
    if lst is None:
        lst = []
        tmp = n
    else:
        if sum(lst) == n:
            return set([reduce(lambda x, y: x*y, lst)])
        tmp = lst[-1]
    results = set()
    for i in reversed(xrange(1, tmp + 1)):
        if sum(lst) + i <= n:
            a = partitions(n, lst + [i])
            results.update(a)
    return results


def part(n):
    p = sorted(partitions(n))
    return "Range: %s Average: %.2f Median: %.2f" % (range_(p), avg(p), median(p))

