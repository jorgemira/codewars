"""
Codewars 6 kyu kata: Sum of Intervals
URL: https://www.codewars.com/kata/52b7ed099cdc285c300001cd/python
"""


def sum_of_intervals(intervals):
    r = 0
    while intervals:
        i = intervals.pop()
        for n, x in enumerate(intervals):
            if (x[0] <= i[0] <= x[1] or x[0] <= i[1] <= x[1] or
                i[0] <= x[0] <= i[1] or i[0] <= x[1] <= i[1]):
                del intervals[n]
                intervals.append((min(x[0],i[0]), max(x[1],i[1]))) 
                break
        else:
            r += i[1] - i[0]
    return r

