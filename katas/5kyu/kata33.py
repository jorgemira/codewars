"""
Codewars 5 kyu kata: Pick peaks
URL: https://www.codewars.com/kata/5279f6fe5ab7f447890006a7/python
"""


def pick_peaks(arr):
    result = {"pos": [], "peaks": []}
    if not arr:
        return result

    tmp = [(i,x) for i, x in enumerate(arr) if not i or arr[i-1] != x]

    for i in xrange(1, len(tmp) -1):
        if tmp[i][1] > tmp[i-1][1] and tmp[i][1] > tmp[i+1][1]:
            result["pos"].append(tmp[i][0])
            result["peaks"].append(tmp[i][1])

    return result

