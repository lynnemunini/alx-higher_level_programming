#!/usr/bin/python3
'''Class Square that defines a square'''


class Square:
    '''Class Square that defines a square with attribute size'''
    def __init__(self, size):
        '''The size of a square is crucial for a square, many things depend \
        of it (area computation, etc.). It is important to keep to keep \
        this value private so as to ensure the class builder controls \
        the type and value of this attribute'''
        self.__size = size
