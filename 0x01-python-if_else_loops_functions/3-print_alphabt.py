#!/usr/bin/python3
def lower_alpha():
    for c in range(97, 123):
        if c != 101 and c != 113:
            print("{:c}".format(c), end="")
lower_alpha()
