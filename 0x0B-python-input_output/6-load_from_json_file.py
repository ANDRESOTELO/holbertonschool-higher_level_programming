#!/usr/bin/python3
"""Create object from a JSON file"""

import json


def load_from_json_file(filename):
    """
    Function that creates an
    Object from a JSON file
    """

    with open(filename, 'r') as f:
        read_file = f.read()
        return json.loads(read_file)
