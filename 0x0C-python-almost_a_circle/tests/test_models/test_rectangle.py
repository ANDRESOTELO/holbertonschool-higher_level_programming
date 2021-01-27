#!/usr/bin/python3
'''
Unittest for rectangle.py module
'''

import unittest
import pep8
import io
from contextlib import redirect_stdout
from models.base import Base, __doc__
from models.rectangle import Rectangle
from models.base import Base


class TestRectangle(unittest.TestCase):
    '''
    Define TestRectangle class
    '''
    def test_doc_string(self):
        '''
        Test docstring
        '''
        self.assertIsNotNone(Rectangle.__doc__)

    def test_pep8_Rectangle(self):
        '''
        Test that checks pep8 implementation
        '''
        style_rec = pep8.StyleGuide(quiet=True)
        check_rec = style_rec.check_files(['models/rectangle.py'])
        self.assertEqual(check_rec.total_errors, 0,
                         "PEP8 style errors: {:d}"
                         .format(check_rec.total_errors))

    def test_pep8_test_rectangle(self):
        '''
        Test that checks pep8 implementation in test_rectangle file
        '''
        style = pep8.StyleGuide(quiet=True)
        check = style.check_files(['tests/test_models/test_rectangle.py'])
        self.assertEqual(check.total_errors, 0,
                         "PEP8 style errors: {:d}".format(check.total_errors))

    def test_more_parameters(self):
        '''
        Test create instance with more than 6 params
        '''
        with self.assertRaises(TypeError):
            r1 = Rectangle(10, 2, 0, 0, 12, 25, 45)

    def test_id_instance(self):
        '''
        Test that chekcs correct creation of instance
        checking correct id instance and specific id too.
        We can assume id is an integer an don´t need to
        test the type of it
        '''
        r1 = Rectangle(5, 4)
        self.assertEqual(r1.id, 1)
        r2 = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(r2.id, 12)

    def test_parameters(self):
        '''
        Test parameters in instance
        '''
        r3 = Rectangle(10, 2, 0, 0)
        self.assertEqual([r3.width, r3.height, r3.x, r3.y], [10, 2, 0, 0])
        self.assertEqual(r3.id, 1)

        r4 = Rectangle(15, 25)
        self.assertEqual([r4.x, r4.y, r4.id], [0, 0, 2])

    def test_no_params_instance(self):
        '''
        Test no parameters, only one parameter and more
        parameters in instance
        '''
        with self.assertRaises(TypeError):
            r5 = Rectangle()
        with self.assertRaises(TypeError):
            r6 = Rectangle(1)
        with self.assertRaises(TypeError):
            r7 = Rectangle(None)

    def test_setters(self):
        '''
        Test setters
        '''
        r8 = Rectangle(1, 2)
        r8.width = 10
        self.assertEqual(r8.width, 10)
        r8.height = 20
        self.assertEqual(r8.height, 20)
        r8.x = 30
        self.assertEqual(r8.x, 30)
        r8.y = 40
        self.assertEqual(r8.y, 40)
        self.assertEqual(r8.id, 1)

    def test_set_wrong_value(self):
        '''
        Test set valid value parameter
        '''
        message = " must be an integer"

        try:
            Rectangle("a", 10)
        except TypeError as e:
            self.assertEqual((str(e)), "width" + message)
        try:
            Rectangle(10, "a")
        except TypeError as e:
            self.assertEqual((str(e)), "height" + message)
        try:
            Rectangle(10, 10, "a")
        except TypeError as e:
            self.assertEqual((str(e)), "x" + message)
        try:
            Rectangle(10, 10, 10, "a")
        except TypeError as e:
            self.assertEqual((str(e)), "y" + message)

        message_2 = " must be > 0"
        try:
            Rectangle(-5, 5)
        except ValueError as e:
            self.assertEqual((str(e)), "width" + message_2)
        try:
            Rectangle(5, -5)
        except ValueError as e:
            self.assertEqual((str(e)), "height" + message_2)
        try:
            Rectangle(0, 5)
        except ValueError as e:
            self.assertEqual((str(e)), "width" + message_2)
        try:
            Rectangle(5, 0)
        except ValueError as e:
            self.assertEqual((str(e)), "height" + message_2)

        message_3 = " must be >= 0"
        try:
            Rectangle(3, 4, -2)
        except ValueError as e:
            self.assertEqual((str(e)), "x" + message_3)
        try:
            Rectangle(3, 4, 2, -5)
        except ValueError as e:
            self.assertEqual((str(e)), "y" + message_3)

    def test_area(self):
        '''
        Test area method
        '''
        area_1 = Rectangle(3, 2)
        self.assertEqual(area_1.area(), 6)
        area_3 = Rectangle(8, 7, 0, 0, 12)
        self.assertEqual(area_3.area(), 56)

    def test_display_0(self):
        '''
        Test display method
        '''
        display_1 = Rectangle(2, 2)
        display = (('#' * 2 + '\n') * 2)
        a = io.StringIO()
        with redirect_stdout(a):
            display_1.display()
        output = a.getvalue()
        self.assertEqual(output, display)

    def tearDown(self):
        '''
        Reset counter _nb_objects
        '''
        Base._Base__nb_objects = 0
