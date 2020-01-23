"""
Codewars 6 kyu kata: Calculator
URL: https://www.codewars.com/kata/5235c913397cbf2508000048/python
"""


class Calculator(object):
  def evaluate(self, string):
    return round(eval(string), 3)

