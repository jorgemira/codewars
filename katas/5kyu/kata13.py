"""
Codewars 5 kyu kata: Recover a secret string from random triplets
URL: https://www.codewars.com/kata/53f40dff5f9d31b813000774/python
"""


def recoverSecret(triplets):
    result = ""
    while any(t for t in triplets):
        for f in set(t[0] for t in triplets if t):
            if all(t.index(f) == 0 for t in triplets if f in t):
                result += f
                map(lambda t: t.remove(f) if f in t else None, triplets)
    return result

