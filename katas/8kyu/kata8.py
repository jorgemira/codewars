"""
Codewars 8 kyu kata: String Templates - Bug Fixing #5
URL: https://www.codewars.com/kata/55c90cad4b0fe31a7200001f/python
"""


def build_string(*args):
    return "I like {}!".format(", ".join(args))

