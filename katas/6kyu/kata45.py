"""
Codewars 6 kyu kata: Vasya - Clerk
URL: https://www.codewars.com/kata/555615a77ebc7c2c8a0000b8/python
"""


def tickets(people):
    notes_25 = 0
    notes_50 = 0
    
    for p in people:
        if p == 25:
            notes_25 += 1
        elif p == 50:
            if notes_25:
                notes_25 -= 1
                notes_50 += 1
            else:
                return "NO"
        elif p == 100:
            if notes_50 and notes_25:
                notes_25 -= 1
                notes_50 -= 1
            elif notes_25 > 2:
                notes_25 -= 3
            else:
                return "NO"
    
    return "YES"

