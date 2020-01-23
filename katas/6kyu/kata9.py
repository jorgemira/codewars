"""
Codewars 6 kyu kata: Directions Reduction
URL: https://www.codewars.com/kata/550f22f4d758534c1100025a/python
"""


def dirReduc(arr):
    while True:
        for i in range(len(arr) - 1):
            if ((arr[i] == "NORTH" and arr[i + 1] == "SOUTH") or
                (arr[i] == "SOUTH" and arr[i + 1] == "NORTH") or
                (arr[i] == "EAST" and arr[i + 1] == "WEST") or
                (arr[i] == "WEST" and arr[i + 1] == "EAST")):
                del arr[i]
                del arr[i]
                break
        else:
            break
    return arr

