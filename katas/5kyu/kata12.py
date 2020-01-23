"""
Codewars 5 kyu kata: Can you get the loop ?
URL: https://www.codewars.com/kata/52a89c2ea8ddc5547a000863/python
"""


def loop_size(node):
    i = 0
    nodes = {}
    while node not in nodes:
        nodes[node] = i
        node = node.next
        i += 1
    return i - nodes[node]

