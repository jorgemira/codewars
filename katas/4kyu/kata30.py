"""
Codewars 4 kyu kata: Nesting Structure Comparison
URL: https://www.codewars.com/kata/520446778469526ec0000001/python
"""


def is_list(var):
    return type(var) == type ([])
    
def same_structure_as(original,other):
    if is_list(original) == is_list(other):
        if is_list(original):
            if len(original) != len(other):
                return False
            for i in xrange(len(original)):
                if not same_structure_as(original[i],other[i]):
                    return False
            return True
        return True
    return False

