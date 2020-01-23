"""
Codewars 7 kyu kata: Get your steppin' on son
URL: https://www.codewars.com/kata/55e00266d494ce5155000032/python
"""


def word_step(s):
    words = s.split(" ")
    padding = 0
    tmp = []

    for i, w in enumerate(words):
        if not i % 2:
            tmp.append(' ' * padding + w)
            padding += len(w) -1
        else:
            for l in w[1:-1]:
                tmp.append(' ' * padding + l)

    if not len(words) % 2:
        tmp.append(' ' * padding + s[-1])

    padding += 1

    return [list(t + ' ' * (padding - len(t))) for t in tmp]

