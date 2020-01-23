"""
Codewars 6 kyu kata: A Crazy Robot? Who's is behind the scenes to make that?
URL: https://www.codewars.com/kata/56a313a0538696bcab000004/python
"""


def finaldist_crazyrobot(moves, init_pos):
    final_pos = [init_pos[0], init_pos[1]]

    for move in moves:
        if move[0] == 'U':
            final_pos[1] += move[1]
        elif move[0] == 'D':
            final_pos[1] -= move[1]
        elif move[0] == 'R':
            final_pos[0] += move[1]
        elif move[0] == 'L':
            final_pos[0] -= move[1]

    return ((init_pos[0] - final_pos[0])**2 + (init_pos[1] - final_pos[1])**2) ** .5

