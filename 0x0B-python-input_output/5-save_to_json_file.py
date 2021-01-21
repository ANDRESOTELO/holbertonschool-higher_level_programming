#!/usr/bin/python3
"""Save Object to a file"""

import json


def save_to_json_file(my_obj, filename):
    """
    Function that writes an Object to a
    text file, using a JSON representation
    """

    with open(filename, 'w') as obj_file:
        return obj_file.write(json.dumps(my_obj))
