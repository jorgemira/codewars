"""
Codewars 8 kyu kata: Find The Duplicated Number in a Consecutive Unsorted List
URL: https://www.codewars.com/kata/558dd9a1b3f79dc88e000001/python
"""


def find_dup(arr):
	tmp = [False] * len(arr)
	for i in arr:
		if tmp[i-1]:
			return i
		else:
			tmp[i-1] = True

