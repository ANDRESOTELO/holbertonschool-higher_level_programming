#!/usr/bin/python3
import hidden_4
import sys

if __name__ == '__main__':
    array = dir(hidden_4)
    n = len(array)
    for c in array[0:]:  # Recorre el array hasta el final
        if c[0] != "_":
            print("{:s}".format(c))
