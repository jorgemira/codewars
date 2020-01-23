"""
Codewars 6 kyu kata: Look and say numbers
URL: https://www.codewars.com/kata/53ea07c9247bc3fcaa00084d/python
"""


def look_and_say(data='1', maxlen=5):
    if not maxlen:
        return []

    result, c, n = '', '', 0

    for i in data:
        if i == c:
            n += 1
        else:
            if n:
                result += str(n) + c
            n, c = 1, i
    result += str(n) + c

    return [result] + look_and_say(result, maxlen - 1)

