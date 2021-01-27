#!/usr/bin/python3
'''Base class module'''

import json


class Base:
    '''
    This class will be the "base" of all
    other classes
    '''

    __nb_objects = 0

    def __init__(self, id=None):
        '''Class constructor that have id paramete'''
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        '''Static method that returns the JSON
        string representation of list_dictionaries'''
        if list_dictionaries is None or not list_dictionaries:
            return ("[]")
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        '''Class method that writes the JSON string
        representation of list_objs to a file.
        list_objs is a list of instances who inherits of Base'''
        filename = "{:s}.json".format(cls.__name__)

        # If list_objs is empty
        if list_objs is None:
            new_list = []
        else:
            new_list = []
            # Iterate list_objs
            for obj in list_objs:
                # appends dictionary depends of class
                # calls to_dictionary method
                new_list.append(cls.to_dictionary(obj))
            # converts new_list into a JSON string with static method
            new_list = Base.to_json_string(new_list)
        # create file with empty list if list_objs is empty
        # create and write file with JSON string
        with open(filename, "w") as f:
            f.write(new_list)

    @staticmethod
    def from_json_string(json_string):
        '''Static method that returns the list of the JSON string
        representation json_string'''
        # not json_string checks if string is empty
        if json_string is None or not json_string:
            new_list = []
        else:
            new_list = json.loads(json_string)
        return new_list

    @classmethod
    def create(cls, **dictionary):
        '''Class method that returns an instance with all attributes
        already set'''
        # create an initializing dummy
        dummy = cls(1, 1)
        # update dummy
        cls.update(dummy, **dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        '''Class method that returns a list of isntances'''
        # with cls.__name__ obtains class name
        filename = "{:s}.json".format(cls.__name__)
        new_list = []
        # first open and read file
        with open(filename, 'r') as f:
            # file doesn´t exist return empty list
            if not f:
                return new_list
            else:
                # variable read_file
                read_file = Base.from_json_string(f.read())
            # iterates read_file
            for dictionary in read_file:
                new_list.append(cls.create(**dictionary))
            return new_list
