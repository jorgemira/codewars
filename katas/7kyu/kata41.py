"""
Codewars 7 kyu kata: Selective fear of numbers
URL: https://www.codewars.com/kata/55b1fd84a24ad00b32000075/python
"""


def am_I_afraid(day,num):
    if day == 'Monday':
        return num == 12
    if day == 'Tuesday':
        return num > 95
    elif day == 'Wednesday':
        return num == 34
    elif day == 'Thursday':
        return num == 0
    elif day == 'Friday':
        return not num % 2
    elif day == 'Saturday':
        return num == 56
    elif day == 'Sunday':
        return num in [666, -666]

