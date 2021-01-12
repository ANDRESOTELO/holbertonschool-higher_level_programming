#!/usr/bin/python3
"""Class defines a rectangle"""


class Rectangle:
    """Rectangle class"""

    def __init__(self, width=0, height=0):
        """Initialization"""
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """Get width value"""
        return self.__width

    @property
    def height(self):
        """Get height value"""
        return self.__height

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
        """Set value"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value
