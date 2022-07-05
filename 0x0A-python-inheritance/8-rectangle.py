#!/usr/bin/python3
"""This module creates a class Rectangle that inherits from baseGeometry"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """A class rectangle that inherits from base geometry"""
    def __init__(self, width, height):
        """an initialization function"""
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height
