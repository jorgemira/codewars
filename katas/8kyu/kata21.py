"""
Codewars 8 kyu kata: Collatz Conjecture Length
URL: https://www.codewars.com/kata/54fb963d3fe32351f2000102/python
"""


seqs={1: 1}
def collatz(n):
    '''Returns the number of terms for a given num for the Collatz sequence'''
    if not n in seqs:
        seqs[n] = 1 + collatz(3 * n + 1 if n % 2 else n / 2)
    return seqs[n]

