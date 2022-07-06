#!/usr/bin/python3
""" a module that converts to json"""


import json


def to_json_string(my_obj):
    """a function that converts to json"""
    obj = json.dumps(my_obj)
    return obj
