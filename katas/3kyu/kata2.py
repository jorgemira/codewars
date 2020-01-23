"""
Codewars 3 kyu kata: My smallest code interpreter (aka Brainf**k)
URL: https://www.codewars.com/kata/526156943dfe7ce06200063e/python
"""


def brain_luck(code, input):
    instr_ptr = data_ptr = 0
    data = [0]
    output = ''

    while instr_ptr < len(code):
        if code[instr_ptr] == '>':
            data_ptr += 1
            if data_ptr == len(data):
                data.append(0)
        elif code[instr_ptr] == '<':
            if data_ptr:
                data_ptr -= 1
            else:
                data = [0] + data
        elif code[instr_ptr] == '+':
            data[data_ptr] = (data[data_ptr] + 1) % 256
        elif code[instr_ptr] == '-':
            data[data_ptr] = (data[data_ptr] - 1) % 256
        elif code[instr_ptr] == '.':
            output += chr(data[data_ptr])
        elif code[instr_ptr] == ',':
            data[data_ptr], input = ord(input[0]), input[1:]
        elif code[instr_ptr] == '[':
            if not data[data_ptr]:
                scope = 1
                while scope:
                    instr_ptr += 1
                    if code[instr_ptr] == '[':
                        scope += 1
                    elif code[instr_ptr] == ']':
                        scope -= 1
        elif code[instr_ptr] == ']':
            if data[data_ptr]:
                scope = 1
                while scope:
                    instr_ptr -= 1
                    if code[instr_ptr] == ']':
                        scope += 1
                    elif code[instr_ptr] == '[':
                        scope -= 1
                        
        instr_ptr += 1

    return output

