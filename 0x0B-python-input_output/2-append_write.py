#!/usr/bin/python3
"""
Module that has a function that
appends a string to a text file (UTF8) and
returns the number of characters written
"""


def append_write(filename="", text=""):
    """
    function that appends a string to a text file (UTF8) and returns the number
    of characters written
    """
    with open(filename, encoding="utf-8", mode="a") as f:
        return f.write(text)
