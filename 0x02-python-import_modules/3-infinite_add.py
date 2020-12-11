#!/usr/bin/python3
import sys

if __name__ == '__main__':
    n = len(sys.argv)  # length of argv counting program
    argv_index = sys.argv  # set argv arguments in an array
    sum = 0
    for i in range(1, n):
        sum = sum + int(argv_index[i])
    print("{:d}".format(sum))
