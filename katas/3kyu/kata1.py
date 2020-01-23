"""
Codewars 3 kyu kata: Valid Braces
URL: https://www.codewars.com/kata/5277c8a221e209d3f6000b56/python
"""


def validBraces(string):
    stack = []
    for c in string:
        if c in '([{':
            stack.append(c)
        elif stack and abs(ord(c) - ord(stack.pop())) > 2:
            return False
    return not stack

