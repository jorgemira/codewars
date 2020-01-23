"""
Codewars 5 kyu kata: Ookkk, Ok, O? Ook, Ok, Ooo!
URL: https://www.codewars.com/kata/55035eb47451fb61c0000288/python
"""


def okkOokOo(s):
    ok, ook= '', ''
    for o in s:
        if o in "Oo":
            ok += '0'
        elif o == 'k':
            ok += '1'
        else:
            if len(ok) == 8:
                ook += chr(int(ok, 2))
                ok = ''
            elif len(ok) > 8:
                ook += chr(int('0' + ok[:7], 2))
                ok = ok[7:]
    return ook

