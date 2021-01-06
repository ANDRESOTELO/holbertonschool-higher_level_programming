#!/usr/bin/python3
"""Program to define a square (based on 4-square.py)"""


class Square:
    """Class that defines a square"""

    def __init__(self, size=0):
        self.__size = size

    @property
    def size(self, size=0):
        return self.__size

    @size.setter
    def size(self, size=0):
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def my_print(self):
        if self.__size == 0:
            print()
        else:
            for x in range(self.__size):
                for x in range(self.__size):
                    print("#", end="")
                print()
