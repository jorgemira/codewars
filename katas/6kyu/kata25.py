"""
Codewars 6 kyu kata: Design a Simple Automaton (Finite State Machine)
URL: https://www.codewars.com/kata/5268acac0d3f019add000203/python
"""


class Automaton(object):
    """
    q1 is our start state. We begin reading commands from here.
    q2 is our accept state. We return true if this is our last state.

    q1 moves to q2 when given a 1, and stays at q1 when given a 0.
    q2 moves to q3 when given a 0, and stays at q2 when given a 1.
    q3 moves to q2 when given a 0 or 1.

Our automaton should return whether
    """
    def __init__(self):
        self.state = 1

    def read_commands(self, commands):
        for c in commands:
            if self.state == 1:
                self.state = 2 if c == "1" else 1
            elif self.state == 2:
                self.state = 3 if c == "0" else 1 if c == '0' else 2
            else:
                self.state = 2
        return self.state == 2
# Return True if we end in our accept state, False otherwise

my_automaton = Automaton()

