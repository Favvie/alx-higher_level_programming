#!/usr/bin/python3
"""This module contains a square class"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """A class square that inherits from base rectangle"""
    def __init__(self, size):
        """an initialization function"""
        super().integer_validator(size, size)
        self.__size = size

    def area(self):
        """a function that calculates an area"""
        return self.__size * self.__size

    def __str__(self):
        """modify the string representation of rectangle instance"""
        return("[Square] {}/{}".format(self.__size, self.__size))
