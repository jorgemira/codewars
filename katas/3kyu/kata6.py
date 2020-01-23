"""
Codewars 3 kyu kata: Convert PascalCase string into snake_case
URL: https://www.codewars.com/kata/529b418d533b76924600085d/python
"""


def to_underscore(string):
    return ''.join(('_' if c.isupper() and i else '') + c.lower() for i, c in enumerate(str(string)))

