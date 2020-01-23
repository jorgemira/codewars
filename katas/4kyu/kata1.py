"""
Codewars 4 kyu kata: Esolang: Ticker
URL: https://www.codewars.com/kata/5876e24130b45aaa0c00001d/python
"""


def interpreter(tape):
    sel = 0
    cells = [0]
    otape = []
        
    for c in tape:
        if c == '>':
            sel += 1
        elif c == '<':
            sel -= 1
        elif c == '*':
            otape.append(chr(cells[sel] if 0 <= sel < len(cells) else 0))
        elif c == '+' and 0 <= sel < len(cells):
            cells[sel] = (cells[sel] + 1) % 256
        elif c == '-' and 0 <= sel < len(cells):
            cells[sel] = (cells[sel] - 1) % 256
        elif c == '/' and 0 <= sel < len(cells):
            cells[sel] = 0
        elif c == '!':
            cells.append(0)

    return ''.join(otape)

