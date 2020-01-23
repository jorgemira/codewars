"""
Codewars 7 kyu kata: Count by X
URL: https://www.codewars.com/kata/5513795bd3fafb56c200049e/python
"""


def count_by(x, n):
   return [x*(i+1) for i in xrange(n)]

