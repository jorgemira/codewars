"""
Codewars 6 kyu kata: Strip Comments
URL: https://www.codewars.com/kata/51c8e37cee245da6b40000bd/python
"""


def solution(string,markers):
    result = []
    for line in string.split('\n'):
        for m in markers:
            try:
                line = line[:line.index(m)]
            except ValueError:
                pass
        result.append(line.rstrip())    
    return '\n'.join(result)

