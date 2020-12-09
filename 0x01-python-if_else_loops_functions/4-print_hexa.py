#!/usr/bin/python3
def hexadecimal():
    for n in range(0, 99):
        print("{:d} = ".format(n) + hex(n))
hexadecimal()
