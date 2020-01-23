"""
Codewars 4 kyu kata: The observed PIN
URL: https://www.codewars.com/kata/5263c6999e0f40dee200059d/python
"""


KEYS = {'0': ['0', '8'],
        '1': ['1', '2', '4'],
        '2': ['1', '2', '3', '5'],
        '3': ['2', '3', '6'],
        '4': ['1', '4', '5', '7'],
        '5': ['2', '4', '5', '6', '8'],
        '6': ['3', '5', '6', '9'],
        '7': ['4', '7', '8'],
        '8': ['5', '7', '8', '9', '0'],
        '9': ['6', '8', '9']}

def get_pins(observed):
    return [k + p for p in get_pins(observed[1:]) for k in KEYS[observed[0]]] if observed else ['']

