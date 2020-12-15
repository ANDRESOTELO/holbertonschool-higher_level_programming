#!/usr/bin/python3
def element_at(my_list, idx):
    if idx < 0:
        return None
    for n in range(len(my_list)):
        if n == idx:
            return my_list[n]
        elif n > idx:
            return None
