"""
Codewars 7 kyu kata: sum2total
URL: https://www.codewars.com/kata/559fed8454b12433ff0000a2/python
"""


def total(arr):
    return total([arr[i] + arr[i+1] for i in xrange(len(arr) - 1)]) if len(arr) != 1 else arr[0]

