#!/usr/bin/python3
"""This module creates a class Rectangle that inherits from baseGeometry"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """A class rectangle that inherits from base geometry"""
    def __init__(self, width, height):
        """an initialization function"""
        self.integer_validator(width, width)
        self.__width = width
        self.integer_validator(height, height)
        self.__height = height

    def area(self):
        """a function that calculates an area"""
        return self.__width * self.__height

    def __str__(self):
        """modify the string representation of rectangle instance"""
        return("[Rectangle] {}/{}".format(self.__width, self.__height))
