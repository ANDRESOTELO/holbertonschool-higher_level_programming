#!/usr/bin/python3
"""Function that writes a string"""


def write_file(filename="", text=""):
    """
    Function that writes a string
    to a text file (UTF8) and returns
    the number of characters written
    """

    with open(filename, 'w') as input_text:
        num_chars = input_text.write(text)
        return (num_chars)
