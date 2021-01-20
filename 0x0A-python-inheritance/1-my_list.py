#!/usr/bin/python3
"""Classes and Inheritance"""


class MyList(list):
    """Class that inherits from list"""

    def print_sorted(self):
        """Method that prints the list"""

        sort_list = sorted(self)
        print(sort_list)
