#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    count = len(my_list)
    if idx < 0:
        return my_list
    if count < idx:
        return my_list
    for n in range(count):
        if idx == n:
            my_list[n] = element
            return my_list
