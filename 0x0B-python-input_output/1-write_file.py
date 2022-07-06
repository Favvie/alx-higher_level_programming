#!/usr/bin/python3
""" a module that writes file """


def write_file(filename="", text=""):
    """ a function that writes to a file"""
    with open(filename, mode='w', encoding="utf-8") as f:
        nb = f.write(text)
        return nb
