"""
Codewars 5 kyu kata: Battleship field validator
URL: https://www.codewars.com/kata/52bb6539a4cf1b12d90005b7/python
"""


BOARD_SIZE = 10


def ship_size(field, x, y):
    size = 1
    field[x][y] = 2

    if x != BOARD_SIZE - 1:
        if field[x][y + 1] == 1:  # Ship is horizontal
            while x + size != BOARD_SIZE - 1 and field[x][y + size] == 1:
                field[x][y + size] = 2
                size += 1
                if y != BOARD_SIZE - 1 and field[x + 1][y + size] != 0:
                    return None
            if sum(([field[x - 1][y - 1]] if x and y else [0]) +
                   ([field[x + 1][y - 1]] if x + 1 < BOARD_SIZE and y else [0]) +
                   ([field[x + 1][y + size]] if x + 1 < BOARD_SIZE and y + size < BOARD_SIZE else [0]) +
                   ([field[x - 1][y + size]] if x and y + size < BOARD_SIZE else [0])):
                return None
        elif field[x][y + 1] == 2:
            return None
    if y != BOARD_SIZE - 1:
        if field[x + 1][y] == 1:  # Ship is vertical
            while x + size != BOARD_SIZE - 1 and field[x + size][y] == 1:
                field[x + size][y] = 2
                size += 1
                if x != BOARD_SIZE - 1 and field[x + size][y + 1] != 0:
                    return None
            if sum(([field[x - 1][y - 1]] if x and y else [0]) +
                   ([field[x - 1][y + 1]] if x and y + 1 < BOARD_SIZE else [0]) +
                   ([field[x + size][y + 1]] if x + size < BOARD_SIZE and y + 1 < BOARD_SIZE else [0]) +
                   ([field[x + size][y - 1]] if x + size < BOARD_SIZE and y else [0])):
                return None
        elif field[x + 1][y] == 2:
            return None

    if size == 1:  # Submarine
        if sum(([field[x - 1][y - 1]] if x and y else [0]) +
               ([field[x + 1][y - 1]] if x + 1 < BOARD_SIZE and y else [0]) +
               ([field[x - 1][y + 1]] if x and y + 1 < BOARD_SIZE else [0]) +
               ([field[x + 1][y + 1]] if x + 1 < BOARD_SIZE and y + 1 < BOARD_SIZE else [0])):
            return None

    return size


def validateBattlefield(field):
    navy = {1: 4,  # submarines
            2: 3,  # destroyers
            3: 2,  # cruisers
            4: 1}  # battleship

    for x in xrange(BOARD_SIZE):
        for y in xrange(BOARD_SIZE):
            if field[x][y] == 1:
                ship = ship_size(field, x, y)
                if ship not in navy:
                    return False
                navy[ship] -= 1

    return not any(navy.values())

