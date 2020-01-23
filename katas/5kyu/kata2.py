"""
Codewars 5 kyu kata: Escape with your booty!
URL: https://www.codewars.com/kata/5b0560ef4e44b721850000e8/python
"""


class SeaMap:
    def __init__(self, board):
        self.height = len(board)
        self.width = len(board[0])
        self.pirate_ship = None
        self.navy_ships = []
        for y, row in enumerate(board):
            for x, c in enumerate(row):
                if c == 'N':
                    self.navy_ships.append(NavyShip(x, y, self.height))
                elif c == 'X':
                    self.pirate = PirateShip(x, y, self.width)

    def __iter__(self):
        return self

    def next(self):
        self.pirate.next()
        for n in self.navy_ships:
            n.next()

    def is_safe(self):
        for n in self.navy_ships:
            if (abs(n.x - self.pirate.x) <= 1 and
                abs(n.y - self.pirate.y) <= 1):
                return False
        return True


class Ship:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __iter__(self):
        return self

    def next(self):
        raise NotImplementedError


class NavyShip(Ship):
    def __init__(self, x, y, height):
        super().__init__(x, y)
        self.height = height
        self.down = y == 0

    def next(self):
        if self.y == 0:
            self.y += 1
            self.down = True
        elif self.y == self.height - 1:
            self.y -= 1
            self.down = False
        else:
            self.y += 1 if self.down else -1


class PirateShip(Ship):
    def __init__(self, x, y, width):
        super().__init__(x, y)
        self.width = width

    def next(self):
        if self.x == self.width - 1:
            raise StopIteration
        else:
            self.x += 1


def check_course(sea_map):
    m = SeaMap(sea_map)
    while m.is_safe():
        try:
            m.next()
        except StopIteration:
            return True
    return False

