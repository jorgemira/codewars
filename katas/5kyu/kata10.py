"""
Codewars 5 kyu kata: Human readable duration format
URL: https://www.codewars.com/kata/52742f58faf5485cae000b9a/python
"""


def format_duration(seconds):
    if not seconds:
        return 'now'

    items = [['second', 60], ['minute', 60], ['hour', 24], ['day', 365]]
    for item in items:
        item.append(seconds % item[1])
        seconds /= item[1]
    items.append(['year', None, seconds])

    tmp = [' '.join([str(item[2]), item[0] + ('' if item[2] == 1 else 's')]) for item in items if item[2]]
    return ' and '.join([', '.join(reversed(tmp[1:])), tmp[0]]) if len(tmp) > 1 else tmp[0]

