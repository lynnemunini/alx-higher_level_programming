#!/usr/bin/python3
'''Class Square that defines a square'''


class Square:
    '''Class Square that defines a square with attribute size'''
    def __init__(self, size=0):
        '''The size of a square is crucial for a square, many things depend \
        of it (area computation, etc.). It is important to keep to keep \
        this value private so as to ensure the class builder controls \
        the type and value of this attribute'''
        self.__size = size

        if type(self.__size) != int:
           raise TypeError("size must be an integer")
        if self.__size < 0:
           raise ValueError("size must be >= 0")
