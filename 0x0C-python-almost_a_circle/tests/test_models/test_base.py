#!/usr/bin/python3
'''
Unittest for base.py module
'''

import unittest
import json
import pep8
import inspect
from models.base import Base, __doc__
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
    '''
    Define TestBase class
    '''
    def test_pep8_Base(self):
        '''
        Test that checks pep8 implementation
        '''
        style = pep8.StyleGuide(quiet=True)
        check = style.check_files(['models/base.py'])
        self.assertEqual(check.total_errors, 0,
                         "PEP8 style errors: {:d}".format(check.total_errors))

    def test_pep8_test_base(self):
        '''
        Test that checks pep8 implementation in test_base file
        '''
        style = pep8.StyleGuide(quiet=True)
        check = style.check_files(['tests/test_models/test_base.py'])
        self.assertEqual(check.total_errors, 0,
                         "PEP8 style errors: {:d}".format(check.total_errors))

    def test_private_class_var(self):
        '''
        Testing if __nb_objects is private
        '''
        with self.assertRaises(AttributeError):
            print(Base.__nb_objects)

    def test_more_parameters(self):
        '''
        Test create instance with more than 6 params
        '''
        with self.assertRaises(TypeError):
            rectangle = Base(10, 2, 0, 0, 12, 25, 45)

    def test_create_instance(self):
        '''
        Test that chekcs correct creation of instance
        checking correct id instance and specific id too.
        We can assume id is an integer an don´t need to
        test the type of it
        '''
        instance = Base()
        self.assertEqual(instance.id, 1)
        instance = Base()
        self.assertEqual(instance.id, 2)
        instance = Base(12)
        self.assertEqual(instance.id, 12)
        instance = Base()
        self.assertEqual(instance.id, 3)
        instance = Base(-8)
        self.assertEqual(instance.id, -8)

    def test_to_json_string(self):
        '''
        Test static method to json_string
        empty list of dictionaries
        '''
        json_dictionary = Base.to_json_string([])
        self.assertEqual(json_dictionary, "[]")

    def test_to_json_string_B(self):
        '''
        Second test to static method json_string
        '''
        r1 = Rectangle(10, 7, 2, 8)
        dictionary = r1.to_dictionary()
        new_json_dict = {'width': 10, 'height': 7, 'x': 2, 'y': 8}
        json_dictionary = Base.to_json_string([dictionary])
        self.assertEqual(type(dictionary), dict)
        self.assertEqual(type(json_dictionary), str)

    def test_save_to_file(self):
        '''
        Test to save to file method
        '''
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file([r1, r2])
        with open("Rectangle.json", "r") as file:
            self.assertEqual([r1.to_dictionary(),
                              r2.to_dictionary()], json.load(file))

    def test_save_to_file_2(self):
        '''
        Test to save to file method with empty file
        '''
        Rectangle.save_to_file([])
        with open("Rectangle.json", "r") as file:
            self.assertEqual([], json.load(file))

    def test_from_json_string(self):
        '''
        Test to from_json_string method with empty file
        '''
        self.assertEqual(Base.from_json_string(None), [])

    def test_from_json_string(self):
        '''
        Test to from_json_string method
        '''
        list_input = [{'id': 89, 'width': 10, 'height': 4}]
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)
        self.assertEqual(type(list_input), list)
        self.assertEqual(type(json_list_input), str)
        self.assertEqual(type(list_output), list)

    def tearDown(self):
        '''
        Reset counter _nb_objects
        '''
        Base._Base__nb_objects = 0
