#!/usr/bin/python3
"""From JSON string to Object"""

import json
"""import json module"""


def from_json_string(my_str):
    """
    Function that returns an object
    (Python data structure) represented
    by a JSON string
    """

    python_object = json.loads(my_str)
    return python_object
