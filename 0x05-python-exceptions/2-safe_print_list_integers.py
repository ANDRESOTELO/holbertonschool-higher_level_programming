#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    count = 0
    for data in range(x):
        try:
            int(data)
            print("{:d}".format(my_list[data]), end='')
            count = count + 1
        except (ValueError, TypeError):
            continue
    print()
    return(count)
