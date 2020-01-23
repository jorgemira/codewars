"""
Codewars 8 kyu kata: Number of People in the Bus
URL: https://www.codewars.com/kata/5648b12ce68d9daa6b000099/python
"""


def number(bus_stops):
    return sum(on - off for on, off in bus_stops)

