#!/usr/bin/python3
'''Rectangle module'''

from models.base import Base


class Rectangle(Base):
    '''Class that inherits from "Base" class'''

    def __init__(self, width, height, x=0, y=0, id=None):
        '''
        Rectangle class constructor
        that receive 4 arguments and
        inherits a super class argument
        '''
        Base.__init__(self, id)
        if type(width) is not int:
            raise TypeError('width must be an integer')
        elif width <= 0:
            raise ValueError('width must be > 0')
        else:
            self.__width = width

        if type(height) is not int:
            raise TypeError('height must be an integer')
        elif height <= 0:
            raise ValueError('height must be > 0')
        else:
            self.__height = height

        if type(x) is not int:
            raise TypeError('x must be an integer')
        elif x < 0:
            raise ValueError('x must be >= 0')
        else:
            self.__x = x

        if type(y) is not int:
            raise TypeError('y must be an integer')
        elif y < 0:
            raise ValueError('y must be >= 0')
        else:
            self.__y = y

    @property
    def width(self):
        '''Get __width value'''
        return self.__width

    @width.setter
    def width(self, value):
        '''Set value to a private atribute __width'''
        if type(value) is not int:
            raise TypeError('width must be an integer')
        elif value <= 0:
            raise ValueError('width must be > 0')
        else:
            self.__width = value

    @property
    def height(self):
        '''Get __height value'''
        return self.__height

    @height.setter
    def height(self, value):
        '''Set value to a private atribute __height'''
        if type(value) is not int:
            raise TypeError('height must be an integer')
        elif value <= 0:
            raise ValueError('height must be > 0')
        else:
            self.__height = value

    @property
    def x(self):
        '''Get __x value'''
        return self.__x

    @x.setter
    def x(self, value):
        '''Set value to a private atribute __x'''
        if type(value) is not int:
            raise TypeError('x must be an integer')
        elif value < 0:
            raise ValueError('x must be >= 0')
        else:
            self.__x = value

    @property
    def y(self):
        '''Get __y value'''
        return self.__y

    @y.setter
    def y(self, value):
        '''Set value to a private atribute __y'''
        if type(value) is not int:
            raise TypeError('x must be an integer')
        elif value < 0:
            raise ValueError('y must be >= 0')
        else:
            self.__y = value

    def area(self):
        '''Public method that returns the area value of the
        Rectangle instance'''
        return self.__width * self.__height

    def display(self):
        '''Public method that prints in stdout the Rectangle
        instance with character "#"'''
        for row_space in range(self.__y):
            print()
        for row in range(self.__height):
            print('{}{}'.format(' '*self.__x, '#'*self.__width))

    def __str__(self):
        '''Method that override the __str__ method and
        returns specific text format'''
        str_overriding = '[Rectangle] ({:d}) {:d}/{:d} - {:d}/{:d}'
        return (str_overriding.format(self.id, self.__x,
                                      self.__y, self.__width, self.__height))

    def update(self, *args, **kwargs):
        '''Public method that assigns an argument to each attribute
        **kwargs assigns key/value arguments to attributes'''
        # object to update with setattr()
        to_update = ['id', 'width', 'height', 'x', 'y']

        if args:
            for i in range(len(args)):
                # setattr() sets the value of the attribute of an object
                # the sintax is setattr(objetc, name, value)
                setattr(self, to_update[i], args[i])
        if kwargs:
            for key in kwargs:
                setattr(self, key, kwargs[key])

    def to_dictionary(self):
        '''Public method that returns the dictionary
        representation of a Rectangle'''
        atributes_dict = {'id': self.id, 'width': self.__width,
                          'height': self.__height, 'x': self.__x,
                          'y': self.__y}
        return atributes_dict
