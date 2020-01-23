"""
Codewars 6 kyu kata: Triangle type
URL: https://www.codewars.com/kata/53907ac3cd51b69f790006c5/python
"""


# Should return triangle type:
#  0 : if triangle cannot be made with given sides
#  1 : acute triangle
#  2 : right triangle
#  3 : obtuse triangle

def triangle_type(a, b, c):
    t = sorted([a, b, c])
    tmp = t[2]**2 - t[1]**2 - t[0]**2
    
    if t[0] + t[1] <= t[2] or t[1] + t[2] <= t[0] or t[0] + t[2] <= t[1]:
        return 0
    elif tmp < 0:
        return 1
    elif tmp > 0:
        return 3
    else:
        return 2

