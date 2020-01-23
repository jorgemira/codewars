"""
Codewars 5 kyu kata: Multiples By Permutations II
URL: https://www.codewars.com/kata/5ba178be875de960a6000187/python
"""


def find_lowest_int(k):
    
    n = 1
    while True:
        if sorted(str(k * n)) == sorted(str((k + 1) * n)):
            return n
        else:
            n += 1

