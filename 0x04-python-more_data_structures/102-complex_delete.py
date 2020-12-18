#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    for key, origin_val in list(a_dictionary.items()):
        if origin_val == value:
            del a_dictionary[key]
    return a_dictionary
