"""
Codewars 4 kyu kata: Snail
URL: https://www.codewars.com/kata/521c2db8ddc89b9b7a0000c1/python
"""


def snail(array):
    result = []
    while array:
        result += array.pop(0)
        array = zip(*array)[::-1]
    return result

