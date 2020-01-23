"""
Codewars 4 kyu kata: Roman Numerals Helper
URL: https://www.codewars.com/kata/51b66044bce5799a7f000003/python
"""


from string import maketrans


class RomanNumerals:
    r2n = {'1': 'a', '2': 'aa', '3': 'aaa', '4': 'ab', '5': 'b', '6': 'ba', '7': 'baa', '8': 'baaa', '9': 'ac'}
    n2r = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
    letters = ['M--', 'CDM', 'XLC', 'IVX']
    trantabs = [maketrans('abc', l) for l in letters]

    @classmethod
    def to_roman(cls, n):
        num = ''.join(['0' for _ in xrange(4-len(str(n)))]) + str(n)
        return ''.join(cls.r2n[x].translate(cls.trantabs[i]) for i, x in enumerate(num) if int(x))

    @classmethod
    def from_roman(cls, n):
        nums = [cls.n2r[x] for x in n]
        tot = 0
        for i, x in enumerate(nums):
            sign = 1
            if i < len(nums) - 1 and nums[i] < nums[i+1]:
                sign = -1
            tot += nums[i]*sign
        return tot

