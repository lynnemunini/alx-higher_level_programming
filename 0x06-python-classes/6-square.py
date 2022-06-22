#!/usr/bin/python3
'''Class Square that defines a square'''


class Square:
    '''Class Square that defines a square with attribute size'''
    def __init__(self, size=0, position=(0, 0)):
        '''The size of a square is crucial for a square, many things depend \
        of it (area computation, etc.). It is important to keep to keep \
        this value private so as to ensure the class builder controls \
        the type and value of this attribute. position must be a \
        tuple of 2 positive integers'''
        self.__size = size
        self.__position = position

    def area(self):
        '''Public instance method that returns te current square area'''
        return self.__size * self.__size

    @property
    def size(self):
        '''Retrieve private instance attribute size'''
        return self.__size

    @property
    def position(self):
        '''Retrieve private instance attribute position'''
        return self.__position

    @position.setter
    def position(self, value):
        '''Property setter to change the value of position'''
        if (type(value) != tuple) or (value[0] < 0) or \
                (value[1] < 0) or (type(value[0]) != int) or \
                (type(value[1]) != int):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    @size.setter
    def size(self, value):
        '''Property setter to change the value of size'''
        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def my_print(self):
        '''Prints in stdout the square with the character #'''
        if self.__size == 0:
            print()
        else:
            print("\n" * self.__position[1], end="")
            for i in range(self.__size):
                print(" " * self.__position[0], end="")
                print("#" * self.__size)
