#!/usr/bin/python3
"""
Module that has a function that
returns the JSON representation of an object(string)
"""
import json


def to_json_string(my_obj):
    """
    Function that returns the JSON representation of an object (string)
    """
    return json.dumps(my_obj)
