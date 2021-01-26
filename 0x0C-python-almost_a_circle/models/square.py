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
        return ('[Square] ({:d}) {:d}/{:d} - {:d}'
                .format(self.id, self.x, self.y, self.height))

    @property
    def size(self):
        return self.height

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        to_update = ['id', 'size', 'x', 'y']
        if args:
            for i in range(len(args)):
                setattr(self, to_update[i], args[i])

        if kwargs:
            for key in kwargs:
                setattr(self, key, kwargs[key])

    def to_dictionary(self):
        square_dict = {'id': self.id, 'size': self.height,
                       'x': self.x, 'y': self.y}
        return square_dict
