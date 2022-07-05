#!/usr/bin/python3
"""A module containing the function called is same class"""


def is_same_class(obj, a_class):
    """afunction that compares an object and a given class"""
    if type(obj) is a_class:
        return True
    else:
        return False
