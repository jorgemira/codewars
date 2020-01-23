"""
Codewars 3 kyu kata: Decode the Morse code
URL: https://www.codewars.com/kata/54b724efac3d5402db00065e/python
"""


def decodeMorse(morseCode):
    return ' '.join(''.join(MORSE_CODE[l] for l in w.split(' ')) for w in morseCode.strip().split('   '))

