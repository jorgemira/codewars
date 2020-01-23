"""
Codewars 8 kyu kata: Reducing Problems - Bug Fixing #8
URL: https://www.codewars.com/kata/55d2603d506a40e162000056/python
"""


def calculate_total(t1, t2):
    t1s=reduce(lambda a,b: a+b,t1,0)
    t2s=reduce(lambda a,b: a+b,t2,0)
    return t1s>t2s

