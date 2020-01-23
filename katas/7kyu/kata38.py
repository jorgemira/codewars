"""
Codewars 7 kyu kata: The Coins of Ter | Round to the Next N
URL: https://www.codewars.com/kata/55d38b959f9c33f3fb00007d/python
"""


def adjust(coin, price):
    while price % coin:
        price += 1
    return price

