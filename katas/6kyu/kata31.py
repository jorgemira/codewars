"""
Codewars 6 kyu kata: DNA Sequence Tester
URL: https://www.codewars.com/kata/56fbb2b8fca8b97e4d000a31/python
"""


import string

def check_DNA(seq1, seq2):
    seq2 = seq2[::-1].translate(string.maketrans("ACGT", "TGCA"))
    return seq1 in seq2 or seq2 in seq1

