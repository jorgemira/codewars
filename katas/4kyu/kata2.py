"""
Codewars 4 kyu kata: Did you mean ...?
URL: https://www.codewars.com/kata/5259510fc76e59579e0009d4/python
"""


class Dictionary(object):
    cache = {}

    def __init__(self, words):
        self.words = words

    def find_most_similar(self, term):
        return min(self.words, key=lambda x: self._distance(x, term))

    @staticmethod
    def _distance(s, t):
        if (s, t) not in Dictionary.cache:
            if not s:
                return len(t)
            if not t:
                return len(s)
            cost = 0 if s[-1] == t[-1] else 1
            Dictionary.cache[s, t] = min((Dictionary._distance(s[:-1], t) + 1,
                                          Dictionary._distance(s, t[:-1]) + 1,
                                          Dictionary._distance(s[:-1], t[:-1]) + cost))
        return Dictionary.cache[s, t]

