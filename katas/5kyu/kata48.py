"""
Codewars 5 kyu kata: Online RPG: player to qualifying stage?
URL: https://www.codewars.com/kata/55849d76acd73f6cc4000087/python
"""


def playerRankUp(pts):
     return "Well done! You have advanced to the qualifying stage. Win 2 out of your next 3 games to rank up." if pts >= 100 else False

