"""
Codewars 7 kyu kata: Katastrophe!
URL: https://www.codewars.com/kata/55a3cb91d1c9ecaa2900001b/python
"""


def strong_enough(earthquake, age):
    strength = 1000 * 0.99**age        
    eq = reduce(lambda x, y: x * y, [sum(x) for x in earthquake],1)

    return "Safe!" if strength > eq else "Needs Reinforcement!"

