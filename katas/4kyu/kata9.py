"""
Codewars 4 kyu kata: Simplifying multilinear polynomials
URL: https://www.codewars.com/kata/55f89832ac9a66518f000118/python
"""


from re import finditer

def simplify(poly):
    tmp = {}
    for m in finditer('(\+?|-)(\d*)([a-z]+)', poly):
        mon = [1 if m.groups()[0] != '-' else -1,
               int(m.groups()[1]) if m.groups()[1] else 1,
               ''.join(sorted(m.groups()[2]))]
        tmp[mon[2]] = tmp.get(mon[2], 0) + int(mon[1]) * mon[0]

    result = ''.join(''.join([('+' if tmp[k] > 0 else '-'), (str(abs(tmp[k])) if abs(tmp[k]) != 1 else ''), k])
                     for k in sorted(tmp.keys(), key=lambda x: (len(x), x)) if tmp[k])

    return result[1:] if result.startswith('+') else result

