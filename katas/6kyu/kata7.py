"""
Codewars 6 kyu kata: Sequence of Power Digits Sum
URL: https://www.codewars.com/kata/572f32ed3bd44719f8000a54/python
"""


def sum_pow_dig_seq(start, n, k):

    lst = [start]
    for i in range(1, k + 1):
        lst.append(sum(int(i) ** n for i in str(lst[-1])))

    for i, n in enumerate(lst):
        try:
            p = lst[:i].index(n)
            return [p, lst[p:i], len(lst[p:i]), lst[-1]]
        except ValueError:
            pass

