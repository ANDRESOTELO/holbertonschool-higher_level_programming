#!/usr/bin/python3
"""Program improve geometry"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Class rectangle"""

    def __init__(self, width, height):
        """Class Rectangle Constructor"""

        self.__width = width
        self.__height = height

        self.integer_validator("width", width)
        self.integer_validator('height', height)

    def area(self):
        """Area method"""
        return(self.__width * self.__height)

    def __str__(self):
        return("[Rectangle] {}/{}".format(self.__width, self.__height))
