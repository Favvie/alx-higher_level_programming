#!/usr/bin/python3
"""This is a module for read file function"""
def read_file(filename=''):
    with open(filename, encoding="utf-8") as f:
        f.read()
