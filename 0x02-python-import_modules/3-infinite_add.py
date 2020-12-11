#!/usr/bin/python3
import sys

if __name__ == '__main__':
    n = len(sys.argv)  # length of argv counting program
    argv_index = sys.argv  # set argv arguments in an array
    suma = 0
    for i in range(1, n):
        suma = suma + int(argv_index[i])
    print("{:d}".format(suma))
