"""
Codewars 5 kyu kata: All that is open must be closed...
URL: https://www.codewars.com/kata/55679d644c58e2df2a00009c/python
"""


def is_balanced(source, caps):
    stack = []
    openers = caps[::2]
    closers = caps[1::2]

    for c in source:
        if stack:
            if c in closers and stack[-1] == openers[closers.index(c)]:
                stack.pop()
            elif c in openers:
                stack.append(c)
        else:
            if c in openers:
                stack.append(c)
            elif c in closers:
                return False

    return not len(stack)

