"""
Codewars 4 kyu kata: Codewars style ranking system
URL: https://www.codewars.com/kata/51fda2d95d6efda45e00004e/python
"""


class User(object):
    RANKS = [i for i in xrange(-8, 9) if i]

    def __init__(self):
        self._progress = 0

    @property
    def rank(self):
        return self.RANKS[self._progress / 100] if self._progress / 100 < len(self.RANKS) else self.RANKS[-1]

    @property
    def progress(self):
        return self._progress % 100 if self.rank != self.RANKS[-1] else 0

    def inc_progress(self, rank):
        diff = self.RANKS.index(rank) - self.RANKS.index(self.rank)
        if not diff:
            self._progress += 3
        elif diff == -1:
            self._progress += 1
        elif diff > 0:
            self._progress += 10 * diff ** 2

