#!/usr/bin/python3
"""Program improve geometry"""


class BaseGeometry:
    """Define class BaseGeometry"""

    def area(self):
        """Area method"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates integer
        name is always a string
        value must be an integer
        """
        self.name = name
        self.value = value

        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format(self.name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(self.name))
