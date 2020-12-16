#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if my_list:
        count = len(my_list)
        new = my_list.copy()
        if idx < 0 or idx >= count:
            return my_list
        new[idxx] = element
        return new
