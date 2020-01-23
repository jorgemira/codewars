"""
Codewars 8 kyu kata: Sum up the random string
URL: https://www.codewars.com/kata/55da6c52a94744b379000036/python
"""


import re
def sum_from_string(string):
    p = re.compile('\d+')
    return sum(int(x) for x in p.findall(string))

