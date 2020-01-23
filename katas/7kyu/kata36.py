"""
Codewars 7 kyu kata: Class conundrum - Bug Fixing #7
URL: https://www.codewars.com/kata/55cd4ce59382498cbd000080/python
"""


class List:
    def __init__(self,type):
        self.type=type
        self.items=[]
        self.count=0
    
    def add(self,item):
        if type(item)!=self.type:
            item_type="str" if self.type==str else "int" if self.type==int else "float"
            return "This item is not of type: %s" %(item_type)
        self.items+=[item]
        self.count+=1
        return self

