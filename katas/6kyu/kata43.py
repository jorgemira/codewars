"""
Codewars 6 kyu kata: Detect Pangram
URL: https://www.codewars.com/kata/545cedaa9943f7fe7b000048/python
"""


import string

def is_pangram(s):
    tmp = set(s.lower()) & set(string.ascii_lowercase)
    return ''.join(sorted(tmp)) == string.ascii_lowercase

