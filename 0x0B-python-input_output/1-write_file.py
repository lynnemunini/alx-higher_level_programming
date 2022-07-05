#!/usr/bin/python3
"""
Module that has a function that
writes a string to a text file (UTF8) and
returns the number of characters written
"""


def write_file(filename="", text=""):
    """
    function that writes a string to a text file (UTF8) and returns the number
    of characters written
    """
    with open(filename, encoding="utf-8", mode="w") as f:
        return f.write(text)
