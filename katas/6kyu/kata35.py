"""
Codewars 6 kyu kata: Longest Common Subsequence
URL: https://www.codewars.com/kata/52756e5ad454534f220001ef/python
"""


def lcs(x, y):

    if len(x) > len(y):
        x, y = y, x
    
    if not x:
        return x
        
    # Take the first char if possible
    try: 
        i = y.index(x[:1])
    except ValueError:
        t = ''
    else:
        t = x[:1] + lcs(x[1:], y[i+1:])
    
    # Skip the first char
    nt = lcs(x[1:], y)

    return t if len(t) > len(nt) else nt

