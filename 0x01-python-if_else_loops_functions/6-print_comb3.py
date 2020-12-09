#!/usr/bin/python3
for c in range(0, 10):
    for h in range(c + 1, 10):
        if c != h and c != 8:
            print("{:d}{:d}".format(c, h), end=", ")
        else:
            print("{:d}{:d}".format(c, h))
