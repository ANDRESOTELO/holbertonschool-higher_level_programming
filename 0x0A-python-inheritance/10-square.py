#!/usr/bin/python3
"""Class square that inherits from Rectangle"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Class definition"""

    def __init__(self, size):
        """Class constructor"""

        self.__size = size

        self.integer_validator("size", size)

    def area(self):
        """Area method"""
        return(self.__size * self.__size)
