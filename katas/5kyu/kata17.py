"""
Codewars 5 kyu kata: Befunge Interpreter
URL: https://www.codewars.com/kata/526c7b931666d07889000a3c/python
"""


from random import randint

def interpret(code):
    next_pos = lambda c, dir, x, y: ((x + dir[0]) % len(c), (y + dir[1]) % len(c[x]))
    code = [list(l) for l in code.split('\n')]
    direction = (0, 1)
    x = y = 0
    stack = []
    output = ""

    while code[x][y] != '@':
        c = code[x][y]

        if c in '0123456789':  # 0-9 Push this number onto the stack.
            stack.append(int(c))
        elif c == '+':  # + Addition: Pop a and b, then push a+b.
            stack.append(stack.pop() + stack.pop())
        elif c == '-':  # - Subtraction: Pop a and b, then push b-a.
            stack.append(-stack.pop() + stack.pop())
        elif c == '*':  # * Multiplication: Pop a and b, then push a*b.
            stack.append(stack.pop() * stack.pop())
        elif c == '/':  # / Integer division: Pop a and b, then push b/a, rounded down. If a is zero, push zero.
            a = stack.pop()
            b = stack.pop()
            stack.append(b / a if a else 0)
        elif c == '%':  # % Modulo: Pop a and b, then push the b%a. If a is zero, push zero.
            a = stack.pop()
            b = stack.pop()
            stack.append(b / a if a else 0)
        elif c == '!':  # ! Logical NOT: Pop a value. If the value is zero, push 1; otherwise, push zero.
            stack.append(0 if stack.pop() else 1)
        elif c == '`':  # ` Greater than: Pop a and b, then push 1 if b>a, otherwise push zero.
            stack.append(1 if stack.pop() <= stack.pop() else 0)
        elif c == '>':  # > Start moving right.
            direction = (0, 1)
        elif c == '<':  # < Start moving left.
            direction = (0, -1)
        elif c == '^':  # ^ Start moving up.
            direction = (-1, 0)
        elif c == 'v':  # v Start moving down.
            direction = (1, 0)
        elif c == '?':  # ? Start moving in a random cardinal direction.
            direction = [(0, 1), (0, -1), (-1, 0), (1, 0)][randint(0, 3)]
        elif c == '_':  # _ Pop a value; move right if value = 0, left otherwise.
            direction = (0, -1) if stack.pop() else (0, 1)
        elif c == '|':  # | Pop a value; move down if value = 0, up otherwise.
            direction = (-1, 0) if stack.pop() else (1, 0)
        elif c == '"':  # " Start string mode: push each character's ASCII value all the way up to the next ".
            x, y = next_pos(code, direction, x, y)
            while code[x][y] != '"':
                stack.append(ord(code[x][y]))
                x, y = next_pos(code, direction, x, y)
        elif c == ':':  # : Duplicate value on top of the stack. If there is nothing on top of the stack, push a 0.
            stack.append(stack[-1] if stack else 0)
        elif c == '\\':  # \ Swap two values on top of the stack. If there is only one value, pretend there is an extra
            #  0 on bottom of the stack.
            a = stack.pop() if stack else 0
            b = stack.pop() if stack else 0
            stack.append(a)
            stack.append(b)
        elif c == '$':  # $ Pop value from the stack and discard it.
            stack.pop()
        elif c == '.':  # . Pop value and output as an integer.
            output += str(stack.pop())
        elif c == ',':  # , Pop value and output the ASCII character represented by the integer code that is stored in
            # the value.
            output += chr(stack.pop())
        elif c == '#':  # # Trampoline: Skip next cell.
            x, y = next_pos(code, direction, x, y)
        elif c == 'p':  # p A "put" call (a way to store a value for later use). Pop y, x and v, then change the
            # character at the position (x,y) in the program to the character with ASCII value v.
            x1 = stack.pop()
            y1 = stack.pop()
            code[x1][y1] = chr(stack.pop())
        elif c == 'g':  # g A "get" call (a way to retrieve data in storage). Pop y and x, then push ASCII value of the
            # character at that position in the program.
            x1 = stack.pop()
            y1 = stack.pop()
            stack.append(ord(code[x1][y1]))

        x, y = next_pos(code, direction, x, y)

    return output

