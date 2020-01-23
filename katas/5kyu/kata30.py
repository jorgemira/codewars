"""
Codewars 5 kyu kata: Pete, the baker
URL: https://www.codewars.com/kata/525c65e51bf619685c000059/python
"""


def cakes(recipe, available):
    return min(available.get(ingredient, 0) / recipe[ingredient] for ingredient in recipe)

