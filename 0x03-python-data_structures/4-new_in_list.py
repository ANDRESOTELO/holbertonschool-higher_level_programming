#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    count = len(my_list)
    new = my_list.copy()
    if idx < 0 or idx > count:
        return my_list
    for n in range(count):
        if n == idx:
            new[n] = element
            return new
