"""
Codewars 7 kyu kata: Keypad horror
URL: https://www.codewars.com/kata/5572392fee5b0180480001ae/python
"""


from string import maketrans

def computer_to_phone(numbers):
    return numbers.translate(maketrans("123789", "789123"))

