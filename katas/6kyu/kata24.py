"""
Codewars 6 kyu kata: Coordinates Validator
URL: https://www.codewars.com/kata/5269452810342858ec000951/python
"""


def is_valid_coordinates(coordinates):
    try:
        x, y = tuple(abs(float(c)) for c in coordinates.split(', '))
        return x <= 90 and y <= 180 and 'e' not in coordinates
    except:
        return False

