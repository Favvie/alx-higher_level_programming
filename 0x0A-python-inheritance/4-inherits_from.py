#!/usr/bin/python3
"""This is a module that checks inheritance"""


def inherits_from(obj, a_class):
    """if an object is a subclass of a class"""
    if (issubclass(type(obj), a_class)):
        return True
    else:
        return False
