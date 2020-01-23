"""
Codewars 5 kyu kata: Escape the Mines !
URL: https://www.codewars.com/kata/5326ef17b7320ee2e00001df/python
"""


def directions(map, miner):
    if miner['x'] < len(map) - 1 and map[miner['x'] + 1][miner['y']]:
        yield 'right', {'x': miner['x'] + 1, 'y': miner['y']}
    if miner['y'] < len(map[miner['x']]) - 1 and map[miner['x']][miner['y'] + 1]:
        yield 'down', {'x': miner['x'], 'y': miner['y'] + 1}
    if miner['x'] and map[miner['x'] - 1][miner['y']]:
        yield 'left', {'x': miner['x'] - 1, 'y': miner['y']}
    if miner['y'] and map[miner['x']][miner['y'] - 1]:
        yield 'up', {'x': miner['x'], 'y': miner['y'] - 1}


def solve(map, miner, exit, old_pos=None):
    if miner == exit:
        return []

    for direction, new_pos in directions(map, miner):
        path = solve(map, new_pos, exit, miner) if new_pos != old_pos else None
        if path is not None:
            return [direction] + path

    return None

