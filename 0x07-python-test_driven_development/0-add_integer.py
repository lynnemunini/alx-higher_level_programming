#!/usr/bin/python3

"""
Function that adds 2 integers.
"""


def add_integer(a, b=98):

    """
    Function that adds 2 integers. a and b must be integers or floats,
    otherwise TypeError exception is raised with the message
    a must be an integer or b must be an integer. a and b are also
    casted into integer if they are float.
    """

    if isinstance(a, int) is False and isinstance(a, float) is False:
        raise TypeError("a must be an integer")
    if isinstance(b, int) is False and isinstance(b, float) is False:
        raise TypeError("b must be an integer")
    return int(a) + int(b)
