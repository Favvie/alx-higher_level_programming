#!/usr/bin/python3
"""this is a module that contains is kind class"""


def is_kind_of_class(obj, a_class):
    """compare an object and class """
    if (isinstance(obj, a_class)):
        return True
    else:
        return False
