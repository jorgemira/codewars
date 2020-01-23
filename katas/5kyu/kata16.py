"""
Codewars 5 kyu kata: A Chain adding function
URL: https://www.codewars.com/kata/539a0e4d85e3425cb0000a88/python
"""


class add:
    def __init__(self, n=0):
        self.n = n

    def __call__(self, n):
        return add(self.n + n)

    def __eq__(self, other):
        return self.n == other
        
    def __add__(self, other):
        return self.n + other 
    
    def __sub__(self, other):
        return self.n - other

