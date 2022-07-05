#!/usr/bin/python3
"""This module contains a class Base Geometry"""


class BaseGeometry:
    """A class called base geometry"""
    def area(self):
        """A function that calculates area"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """a function that validates an integer"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        elif value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
