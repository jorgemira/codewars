"""
Codewars 6 kyu kata: Playing with digits
URL: https://www.codewars.com/kata/5552101f47fc5178b1000050/python
"""


def dig_pow(n, p):

    val = sum(int(v) ** (i + p) for i, v in enumerate(str(n)))    
    k = val / float(n)
    
    return k  if k.is_integer() else -1

