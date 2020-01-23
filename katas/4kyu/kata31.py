"""
Codewars 4 kyu kata: Counting Change Combinations
URL: https://www.codewars.com/kata/541af676b589989aed0009e7/python
"""


def count_change(money, coins):
    ways = 0
    if money:
        if coins:
            max_coin = coins[0]
            if money >= max_coin:
                ways += count_change(money - max_coin, coins)
            ways += count_change(money, coins[1:])
        return ways
    else:
        return 1

