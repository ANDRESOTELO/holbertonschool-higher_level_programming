#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    for x in range(list_length):
        try:
            division = my_list_1[x] / my_list_2[x]
        except ZeroDivisionError:
            division = 0
            print("division by 0")
        except TypeError:
            division = 0
            print("wrong type")
        except IndexError:
            division = 0
            print("out of range")
        finally:
            new_list.append(division)
    return (new_list)
