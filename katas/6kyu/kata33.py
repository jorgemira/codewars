"""
Codewars 6 kyu kata: Cumulative Triangle
URL: https://www.codewars.com/kata/5301329926d12b90cc000908/python
"""


cumulative_triangle = lambda n: (n * (n - 1) / 2 + 1) * n + sum(xrange(n))

