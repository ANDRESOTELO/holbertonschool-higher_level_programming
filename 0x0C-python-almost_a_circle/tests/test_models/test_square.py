#!/usr/bin/python3
'''
Unittest for rectangle.py module
'''

import unittest
import pep8
import io
from contextlib import redirect_stdout
from models.base import Base, __doc__
from models.square import Square
from models.base import Base


class TestSquare(unittest.TestCase):
    '''
    Define TestSquare class
    '''
    def test_doc_string(self):
        '''
        Test docstring
        '''
        self.assertIsNotNone(Square.__doc__)

    def test_pep8_Square(self):
        '''
        Test that checks pep8 implementation
        '''
        style = pep8.StyleGuide(quiet=True)
        check = style.check_files(['models/square.py'])
        self.assertEqual(check.total_errors, 0,
                         "PEP8 style errors: {:d}"
                         .format(check.total_errors))

    def test_pep8_test_square(self):
        '''
        Test that checks pep8 implementation in test_square file
        '''
        style = pep8.StyleGuide(quiet=True)
        check = style.check_files(['tests/test_models/test_square.py'])
        self.assertEqual(check.total_errors, 0,
                         "PEP8 style errors: {:d}".format(check.total_errors))

    def test_more_parameters(self):
        '''
        Test create instance with more than 6 params
        '''
        with self.assertRaises(TypeError):
            s1 = Square(10, 2, 0, 0, 12, 25, 45)

    def test_parameters(self):
        '''
        Test parameters in instance
        '''
        s2 = Square(10, 2, 2, 5)
        self.assertEqual(s2.width, 10)
        self.assertEqual(s2.height, 10)
        self.assertEqual(s2.x, 2)
        self.assertEqual(s2.y, 2)
        self.assertEqual(s2.id, 5)

        s3 = Square(5)
        self.assertEqual(s3.width, 5)
        self.assertEqual(s3.height, 5)
        self.assertEqual(s3.x, 0)
        self.assertEqual(s3.y, 0)

        with self.assertRaises(ValueError):
            Square(-4)

        with self.assertRaises(ValueError):
            Square(0)

        with self.assertRaises(TypeError):
            Square("a")

        with self.assertRaises(TypeError):
            Square(5, "a")

        with self.assertRaises(ValueError):
            Square(5, -4)

        with self.assertRaises(TypeError):
            Square(5, 2, "a")

        with self.assertRaises(ValueError):
            Square(5, 2, -5)

        with self.assertRaises(TypeError):
            Square()

    def test_area(self):
        '''
        Test area method
        '''
        area_1 = Square(3)
        self.assertEqual(area_1.area(), 9)
        area_3 = Square(8, 7, 5, 5)
        self.assertEqual(area_3.area(), 64)

    def test_display_0(self):
        '''
        Test display method
        '''
        display_1 = Square(5)
        display = (('#' * 5 + '\n') * 5)
        a = io.StringIO()
        with redirect_stdout(a):
            display_1.display()
        output = a.getvalue()
        self.assertEqual(output, display)

    def test_str(self):
        '''
        Testing the string return
        '''
        s_string = Square(5)
        self.assertEqual(s_string.__str__(), "[Square] (1) 0/0 - 5")

    def test_setter(self):
        '''
        Test the setter
        '''
        set_square = Square(10)
        set_square.size = 50
        self.assertEqual(set_square.__str__(), "[Square] (1) 0/0 - 50")

        set_2 = Square(90)
        with self.assertRaises(TypeError):
            set_2.size = "a"

        set_3 = Square(5, 8, 9, 10)
        with self.assertRaises(ValueError):
            set_3.size = -10

    def test_update(self):
        '''
        Test update method
        '''
        up_1 = Square(5, 8, 9, 10)
        up_1.update(99)
        self.assertEqual(up_1.__str__(), "[Square] (99) 8/9 - 5")
        up_1.update(99, 99)
        self.assertEqual(up_1.__str__(), "[Square] (99) 8/9 - 99")
        up_1.update(99, 99, 99)
        self.assertEqual(up_1.__str__(), "[Square] (99) 99/9 - 99")
        up_1.update(99, 99, 99, 99)
        self.assertEqual(up_1.__str__(), "[Square] (99) 99/99 - 99")

        up_2 = Square(5, 8, 9, 10)
        with self.assertRaises(TypeError):
            up_2.update(99, "a")
        with self.assertRaises(ValueError):
            up_2.update(99, -1)
        with self.assertRaises(ValueError):
            up_2.update(99, 0)

        up_3 = Square(5, 8, 9, 10)
        with self.assertRaises(TypeError):
            up_3.update(99, 5, "a")
        with self.assertRaises(ValueError):
            up_3.update(99, 5, -1)

        up_4 = Square(5, 8, 9, 10)
        with self.assertRaises(TypeError):
            up_4.update(99, 5, 8, "a")
        with self.assertRaises(ValueError):
            up_4.update(99, 5, 8, -1)

    def test_kwargs(self):
        '''
        Test kwargs parameters
        '''
        kwargs = Square(1, 1, 1, 1)
        kwargs.update(size=5, x=5, y=5, id=99)
        self.assertEqual(kwargs.__str__(), "[Square] (99) 5/5 - 5")

    def test_args_kwargs(self):
        '''
        Test args and kwargs
        '''
        test_1 = Square(1, 1, 1, 1)
        test_1.update(10, size=5)
        self.assertEqual(test_1.__str__(), "[Square] (10) 1/1 - 5")

    def tearDown(self):
        '''
        Reset counter _nb_objects
        '''
        Base._Base__nb_objects = 0
