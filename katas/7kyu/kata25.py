"""
Codewars 7 kyu kata: The Owls Are Not What They Seem
URL: https://www.codewars.com/kata/55aa7acc42216b3dd6000022/python
"""


def owl_pic(text):
    p = filter(lambda x: x in "8WTYUIOAHXVM", text.upper())
    return "{}''0v0''{}".format(p, p[::-1])

