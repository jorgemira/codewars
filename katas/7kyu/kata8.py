"""
Codewars 7 kyu kata: The Barksdale Code
URL: https://www.codewars.com/kata/573d498eb90ccf20a000002a/python
"""


def decode(string):
	return string.translate(str.maketrans("1234567890", "9876043215"))

