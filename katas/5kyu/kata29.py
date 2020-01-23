"""
Codewars 5 kyu kata: Mod4 Regex
URL: https://www.codewars.com/kata/54746b7ab2bc2868a0000acf/python
"""


import re

class Mod:
    mod4 = re.compile(r".*\[(\+|-)?(\d*([13579][26]|[02468][048])|[048])\]")

