#!/usr/bin/python3
"""A test for base class"""


import unittest
from models import base
Base = base.Base


class TestBase(unittest.TestCase):
    """a class called testbase"""
    def test_privateAttribute(self):
        """a method that tests if an attribute is private"""
        testInstance = Base()
        with self.assertRaises(AttributeError):
            testInstance.__nb_object

    def test_moduleDocString(self):
        """a method that tests for a modules doc string"""
        self.assertTrue(len(base.__doc__) >= 1)

    def test_classDocString(self):
        """a method that tests for a class docstring"""
        self.assertTrue(len(Base.__doc__) >= 1)

    def test_id(self):
        """a method that tests the id of an instance"""
        testInstanceWithValue = Base(12)
        testInstanceWithoutValue = Base()
        self.assertEqual(testInstanceWithValue.id, 12)
        self.assertEqual(testInstanceWithoutValue.id, 1)

    def test_multipleParameters(self):
        """a method that tests multiple parameters"""
        with self.assertRaises(TypeError):
            testInstance1 = Base(1, 4)
