"""
Codewars 8 kyu kata: International Morse Code Encryption
URL: https://www.codewars.com/kata/55b8c0276a7930249e00003c/python
"""


#CHAR_TO_MORSE preloaded to convert characters into Morse code
def encryption(string):
    return ' '.join([CHAR_TO_MORSE.get(x,x) for x in string])

