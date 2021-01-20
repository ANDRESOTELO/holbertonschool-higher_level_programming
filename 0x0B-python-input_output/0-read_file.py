#!/usr/bin/python3
"""Function that reads a text file"""


def read_file(filename=""):
    """Define function that reads a text file"""

    with open(filename) as text:
        print(text.read(), end="")
