"""
Codewars 5 kyu kata: Elementary Arithmetic - Carries Count
URL: https://www.codewars.com/kata/529fdef7488f509b81000061/python
"""


def solve(input_string):
    result = []
    for pair in input_string.split('\n'):
        x, y = sorted([i[::-1] for i in pair.split(' ')], key=len)
        x += '0' * (len(y) - len(x))
        carries = carry = 0
        for i in xrange(len(x)):
            carry = 1 if int(x[i]) + int(y[i]) + carry > 9 else 0
            carries += carry
        result.append("%s carry operation%s" % ((carries, 's') if carries else ('No', '')))
    return '\n'.join(result)

