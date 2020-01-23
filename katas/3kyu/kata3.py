"""
Codewars 3 kyu kata: Molecule to atoms
URL: https://www.codewars.com/kata/52f831fa9d332c6591000511/python
"""


import re

def normalize(formula, n=1):
    tmp = {}
    for m in re.finditer(r'([A-Z][a-z]?)([0-9]*)', formula):
        tmp[m.group(1)] = tmp.get(m.group(1), 0) + int(m.group(2) or 1) * n
    return tmp

def normalize_str(m):
    return ''.join('%s%s' % (k, v)  for k, v in normalize(m.group(1), int(m.group(2) or 1)).iteritems())

def parse_molecule(formula):
    formula = formula.replace('[', '(').replace('{', '(').replace(']', ')').replace('}', ')')
    while re.search(r'\(', formula):
        formula = re.sub(r'\(([A-Za-z0-9]*)\)([0-9])*', normalize_str, formula)
    return normalize(formula)

