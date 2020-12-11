#!/usr/bin/python3
import sys

if __name__ == '__main__':
    n = len(sys.argv) - 1
    argv_index = sys.argv
    if n == 0:
        str = "arguments."
        print("{:d} ".format(n) + str)
    elif n == 1:
        str = "argument:"
        print("{:d} ".format(n) + str)
        print("{:d}: {:s}".format(n, argv_index[1]))
    else:
        str = "arguments:"
        print("{:d} ".format(n) + str)
        for i in range(1, n + 1):
            print("{:d}: {:s}".format(i, sys.argv[i]))
