#!/usr/bin/python3
"""a module that converts from json to ojbject"""
import json


def from_json_string(my_str):
    """a function that converts form json to object"""
    x = json.loads(my_str)
    return x
