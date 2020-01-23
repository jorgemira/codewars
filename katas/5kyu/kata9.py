"""
Codewars 5 kyu kata: GET TO THE CHOPPA!
URL: https://www.codewars.com/kata/5573f28798d3a46a4900007a/python
"""


def neighbours(grid, node):
    if node.position.x < len(grid) - 1 and grid[node.position.x + 1][node.position.y].passable:
        yield grid[node.position.x + 1][node.position.y]
    if node.position.y < len(grid[node.position.x]) - 1 and grid[node.position.x][node.position.y + 1].passable:
        yield grid[node.position.x][node.position.y + 1]
    if node.position.x and grid[node.position.x - 1][node.position.y].passable:
        yield grid[node.position.x - 1][node.position.y]
    if node.position.y and grid[node.position.x][node.position.y - 1].passable:
        yield grid[node.position.x][node.position.y - 1]


def find_shortest_path(grid, start_node, end_node, cache=None):
    if cache is None:
        cache = {}
    if start_node == end_node:
        return [end_node] if end_node else []
    if start_node not in cache:
        start_node.passable = False
        path = [None] * len(grid) * len(grid[0])
        min_dist = abs(start_node.position.x - end_node.position.x) +  abs(start_node.position.y - end_node.position.y)
        for new_start in neighbours(grid, start_node):
            tmp = find_shortest_path(grid, new_start, end_node, cache)
            if len(tmp) < len(path):
                path = [start_node] + tmp
                start_node.passable = True
            if len(path) - 1 == min_dist:
                break
        cache[start_node] = path
    return cache[start_node]

