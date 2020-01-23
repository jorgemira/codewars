"""
Codewars 8 kyu kata: Does my number look big in this?
URL: https://www.codewars.com/kata/5287e858c6b5a9678200083c/python
"""


def narcissistic( value ):
    str_val = str(value)
    pow = len(str_val)
    
    val = sum([int(v) ** pow for v in str_val])
    
    return val == value

