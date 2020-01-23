"""
Codewars 4 kyu kata: Text align justify
URL: https://www.codewars.com/kata/537e18b6147aa838f600001b/python
"""


def justify(text, width):
    lines = []
    line =[]
    len_line = 0

    for w in text.split():
        if len_line + len(w) > width:
            if len(line) > 1:
                for i in xrange(width - len_line + 1):
                    line[i%(len(line)-1)] += ' '
            lines.append(' '.join(line))
            len_line = 0
            line=[]

        len_line += len(w) +1
        line.append(w)

    lines.append(' '.join(line))
    return '\n'.join(lines)

