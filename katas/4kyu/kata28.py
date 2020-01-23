"""
Codewars 4 kyu kata: IP Validation
URL: https://www.codewars.com/kata/515decfd9dcfc23bb6000006/python
"""


import re

def is_valid_IP(strng):
    so = re.search("^([12]?\d{1,2})\.([12]?\d{1,2})\.([12]?\d{1,2})\.([12]?\d{1,2})$",strng)
    return all(int(g) < 256 for g in so.groups()) if so else False

