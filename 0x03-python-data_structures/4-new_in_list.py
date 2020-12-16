#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if my_list:
        new = my_list.copy()
        count = len(my_list)
        if idx < 0 or idx >= count:
            return my_list
        new[idx] = element
        return new
