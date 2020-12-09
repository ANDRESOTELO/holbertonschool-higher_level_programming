#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
n = number % 10
if number < 0:
    n = number % -10
if n > 5:
    str = "and is greater than 5"
    print("Last digit of {:d} is {:d} {:s}".format(number, n, str))
elif n == 0:
    print("Last digit of {:d} is {:d} and is 0".format(number, n))
else:
    str = "and is less than 6 and not 0"
    print("Last digit of {:d} is {:d} {:s}".format(number, n, str))
