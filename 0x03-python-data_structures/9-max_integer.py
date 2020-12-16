#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list:
        mayor = my_list[0]
        for n in my_list:
            if n > mayor:
                mayor = n
        return mayor
    else:
        return None
