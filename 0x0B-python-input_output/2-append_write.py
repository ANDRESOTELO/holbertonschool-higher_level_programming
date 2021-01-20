#!/usr/bin/python3
"""Append to a file"""


def append_write(filename="", text=""):
    """
    Function that appends a string at the
    end of a text file (UTF8) and returns
    the number of characters added
    """

    with open(filename, 'a') as append_text:
        num_chars = append_text.write(text)
        return num_chars
