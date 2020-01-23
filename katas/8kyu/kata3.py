"""
Codewars 8 kyu kata: Fuel economy converter (mpg <-> L/100 km)
URL: https://www.codewars.com/kata/558aa460dcfb4a94c40001d7/python
"""


gal2l = 3.785411784
m2km = 1.609344


def mpg2lp100km(mpg):
    return float(format(100 * gal2l / mpg / m2km, '.2f'))
    
def lp100km2mpg(lp100km):
    return float(format(100 * gal2l / m2km / lp100km, '.2f'))

