"""
Codewars 4 kyu kata: DNA GC-content
URL: https://www.codewars.com/kata/5747a9bbe2fab9a0c400012f/python
"""


def gc_content(seq):
    return 100 * (seq.count('G') + seq.count('C')) / len(seq) if len(seq) else 0

        
    

Beta
A function within a function


def always(n=0):
    return lambda : n

