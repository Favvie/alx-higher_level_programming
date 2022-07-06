#!/usr/bin/python3
"""a module that writes to a file"""


def read_file(filename=""):
    """ afunction that reads text froma file"""
    with open(filename, mode="r", encoding="utf-8") as f:
        text = f.read()
        print(text)
