#!/usr/bin/python3
def no_c(my_string):
    if my_string:
        new = ""
        for i in my_string:
            if i == "C" or i == "c":
                continue
            new = new + i
        return new
    return my_string
