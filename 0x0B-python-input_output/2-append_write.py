#!/usr/bin/python3
"""this is a that added to a string"""


def append_write(filename="", text=""):
    with open(filename, mode="a", encoding="utf-8") as f:
        nb = f.write(text)
        return nb
