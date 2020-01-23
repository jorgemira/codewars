"""
Codewars 4 kyu kata: Pyramid Slide Down
URL: https://www.codewars.com/kata/551f23362ff852e2ab000037/python
"""


def longest_slide_down(pyramid):
    prev_line = pyramid[-1]

    for i in reversed(xrange(len(pyramid)-1)):
        line = []
        for j in xrange(i+1):
            line.append(pyramid[i][j] + max(prev_line[j], prev_line[j+1]))
        prev_line = line

    return line[0]

