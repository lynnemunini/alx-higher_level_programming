#!/usr/bin/python3
"""Module with a class Student that defines a student"""


class Student:
    def __init__(self, first_name, last_name, age):
        """class Student that defines a student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """retrieves a dictionary representation of a Student"""
        return self.__dict__
