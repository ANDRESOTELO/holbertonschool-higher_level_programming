#!/usr/bin/python3
"""Class defines a rectangle"""


class Rectangle:
    """Rectangle class"""

    def __init__(self, width=0, height=0):
        """Initialization"""

        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = height

        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = width

    @property
    def height(self):
        """Get height value"""
        return self.__height

    @property
    def width(self):
        """Get width value"""
        return self.__width

    @height.setter
    def height(self, value):
        """Set height value"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    @width.setter
    def width(self, value):
        """Set height value"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    def area(self):
        """Instance that returns the area of rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """Instance that returns the perimeter of rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        perim = (self.__width*2) + (self.__height*2)
        return perim

    def __str__(self):
        """Prints rectangle"""
        hash_str = ''
        if self.__width == 0 or self.__height == 0:
            return (hash_str)
        else:
            for row in range(self.__height):
                for item in range(self.__width):
                    hash_str += '#'
                hash_str += '\n'
            return hash_str[0:-1]

    def __repr__(self):
        """Return a string representation"""
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """Delete rectangle"""
        print("Bye rectangle...")
