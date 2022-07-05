#!/usr/bin/python3
"""This is a module """


class MyList(list):
    """this is a class that extends the builtin list"""
    def print_sorted(self):
        """print a sorted form of the list"""
        sorted_list = sorted(self)
        print(sorted_list)
