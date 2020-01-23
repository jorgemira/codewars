"""
Codewars 7 kyu kata: Regex Failure - Bug Fixing #2
URL: https://www.codewars.com/kata/55c423ecf847fbcba100002b/python
"""


from re import sub
def filter_words(phrase):
    return sub("(?i)(bad|mean|ugly|horrible|hideous)","awesome",phrase)

