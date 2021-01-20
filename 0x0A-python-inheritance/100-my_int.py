#!/usr/bin/python3
"""Class MyInt"""


class MyInt(int):
    """A class MyInt that inherits from int"""

    def __eq__(self, other):
        return self.num != other

    def __ne__(self, other):
        return self.num == other
