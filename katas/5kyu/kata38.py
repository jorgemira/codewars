"""
Codewars 5 kyu kata: Max Collatz Sequence Length
URL: https://www.codewars.com/kata/53a9ee602f150d5d6b000307/python
"""


def collatz(num):
    if not getattr(collatz, 'seqs', False):
        setattr(collatz, 'seqs', {1: 1})
    if not num in collatz.seqs:
        collatz.seqs[num] = 1 + collatz(3 * num + 1 if num % 2 else num / 2)
    return collatz.seqs[num]

def max_collatz_length(n):
    if isinstance(n, bool) or not isinstance(n, int) or n <=0:
        return []
    return max(([i, collatz(i)] for i in xrange(1, n + 1)), key=lambda x: x[1])

