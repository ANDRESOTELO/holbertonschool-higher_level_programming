#!/usr/bin/python3
'''Module square'''


from models.rectangle import Rectangle

class Square(Rectangle):
    '''Class square that inherits from Rectangle class'''

    def __init__(self, size, x=0, y=0, id=None):
        '''Class constructor'''
        Rectangle.__init__(self, size, size, x, y, id)

    def __str__(self):
        '''Overload __str__ method from rectangle class'''
        return ('[Square] ({:d}) {:d}/{:d} - {:d}'.format(self.id, self.x, self.y, self.height))

    @property
    def size(self):
        return self.height

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value
