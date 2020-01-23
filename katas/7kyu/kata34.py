"""
Codewars 7 kyu kata: Building blocks
URL: https://www.codewars.com/kata/55b75fcf67e558d3750000a3/python
"""


class Block(object):
    def __init__(self, size):
        self.width = size[0]
        self.length = size[1]
        self.height = size[2]
    
    def get_width(self):
        return self.width

    def get_length(self):
        return self.length

    def get_height(self):
        return self.height
        
    def get_volume(self):
        return self.width * self.length * self.height
    
    def get_surface_area(self):
        return 2 * self.width * self.length  + 2 * self.length * self.height + 2 * self.width * self.height

