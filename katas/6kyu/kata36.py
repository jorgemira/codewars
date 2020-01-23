"""
Codewars 6 kyu kata: Complete The Pattern #14
URL: https://www.codewars.com/kata/559379505c859be5a9000034/python
"""


def pattern(n, y=1, *args):
    
    if y < 1:
        y = 1
    if n < 0:
        return ''
    
    line = lambda x: ''.join(
        [str
         ((x + 1) % 10)
         if x == i or n * 2 - i - 2 == x else
         ' ' for i in xrange(n * 2 - 1)])
    tmp = range(n) + list(reversed(range(1, n-1)))
    result = []
    for x in xrange(2*n-1 + (n-1)*2 * (y-1)):
        result.append(line(tmp[x % ((n-1)*2)]))

    return '\n'.join(result)

