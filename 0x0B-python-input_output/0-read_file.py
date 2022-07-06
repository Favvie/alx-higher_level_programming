#!/usr/bin/python3
"""This is a module for read file function"""


def read_file(filename=""):
    """a function that read files"""
    with open(filename, encoding="utf-8") as f:
        print(f.read())
