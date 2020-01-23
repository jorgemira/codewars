"""
Codewars 7 kyu kata: Complete The Pattern #10 - Parallelogram
URL: https://www.codewars.com/kata/5581a7651185fe13190000ee/python
"""


def pattern(n):

    if n < 1:
        return ''
    sp = lambda x: ''.join([' '] * (x))
    nums = ''.join(str(i%10) for i in xrange(1,n+1))
    c = 2*n-len(nums)
    
    return '\n'.join(sp(c -i -1) + nums + sp(i) for i in xrange(c))

        
    

def pattern(n):
    if n < 1:
        return ''

    sp = lambda x: ''.join([' '] * (x))
    nums = ''.join(str(i % 10) for i in xrange(1,n + 1))
    c = 2 * n - len(nums)
    
    return '\n'.join(sp(c - i - 1) + nums + sp(i) for i in xrange(c))

