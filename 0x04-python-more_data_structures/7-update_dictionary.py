#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    for key_1 in a_dictionary:
        if key == key_1:
            a_dictionary[key] = value
        else:
            up = {key: value}
    a_dictionary.update(up)
    return a_dictionary
