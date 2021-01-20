#!/usr/bin/python3
"""Class MyInt"""


class MyInt(int):
    """A class MyInt that inherits from int"""

    def __eq__(self, num):
        return self.number != num

    def __ne__(self, num):
        return self.number == num
