"""
Codewars 7 kyu kata: Switch/Case - Bug Fixing #6
URL: https://www.codewars.com/kata/55c933c115a8c426ac000082/python
"""


def eval_object(v):
    return {"+": v['a']+v['b'],
        "-": v['a']-v['b'],
        "/": v['a']/v['b'],
        "*": v['a']*v['b'],
        "%": v['a']%v['b'],
        "**": v['a']**v['b'], }.get(v['operation'],1)

