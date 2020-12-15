#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    count = len(my_list)
    if idx < 0:
        return my_list
    if idx > count:
        return my_list
    for n in range(len(my_list)):
        if idx == n:
            my_list[n] = element
            return my_list
