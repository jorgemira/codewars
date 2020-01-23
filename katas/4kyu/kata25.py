"""
Codewars 4 kyu kata: Validate Sudoku with size `NxN`
URL: https://www.codewars.com/kata/540afbe2dc9f615d5e000425/python
"""


class Sudoku(object):

    def __init__(self, sudoku):
        self.sudoku = sudoku
        self.n = len(sudoku)
        self.all_nums = set(range(1, self.n+1))
        self.side = int(self.n**.5)

    def get_row(self, n):
        return self.sudoku[n]

    def get_col(self, n):
        return [self.sudoku[i][n] for i in xrange(self.n)]

    def get_square(self, x, y):
        result = []
        for i in xrange(self.side):
            result.extend(self.get_row(i+x)[y:y+self.side])
        return result

    def is_valid(self):
        if not (float(self.n)**.5).is_integer():
            return False
        if any(len(row) != self.n for row in self.sudoku):
            return False
        if any([isinstance(i, bool) for sl in self.sudoku for i in sl]):
            return False
        if any(self.all_nums - set(self.get_row(n)) for n in xrange(self.n)):
            return False
        if any(self.all_nums - set(self.get_col(n)) for n in xrange(self.n)):
            return False
        for i in xrange(self.side):
            x = i*self.side
            for j in xrange(self.side):
                y = j*self.side
                if self.all_nums - set(self.get_square(x, y)):
                    return False
        return True

