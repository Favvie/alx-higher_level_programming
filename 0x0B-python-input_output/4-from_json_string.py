#!/usr/bin/python3
"""a module that converts from json to ojbject"""
import json


def from_json_string(my_str):
    x = json.loads(my_str)
    return x
