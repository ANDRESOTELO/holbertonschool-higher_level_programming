#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    count = 0
    for data in range(x):
        try:
            print(my_list[data], end='')
            count = count + 1
        except IndexError:
            print()
            return(count)
    print()
    return(count)
