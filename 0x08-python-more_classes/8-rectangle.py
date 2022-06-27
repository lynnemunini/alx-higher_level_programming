#!/usr/bin/python3
"""
Module that has an empty class that defines a rectangle
"""


class Rectangle:
    """
    Class that defines a rectangle
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
        Instantiation
        """
        self.height = height
        self.width = width
        Rectangle.number_of_instances += 1

    def __str__(self):
        """
        Print the rectangle with the character #
        """
        if self.__width == 0 or self.__height == 0:
            return ""
        else:
            shape = ((str(self.print_symbol) * self.__width) + "\n") *\
                     (self.__height)
            return shape[:-1]

    def __repr__(self):
        """
        return a string representation of the rectangle
        """
        return ("Rectangle({}, {})".format(self.__width, self.__height))

    def __del__(self):
        """
        Print the message Bye rectangle... when an instance
        of rectangle is deleted.
        """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @property
    def width(self):
        """
        Property to retrieve private attribute width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        property setter to set the value of width
        width must be an integer, otherwise raise TypeError
        width greater than 0, otherwise raise ValueError
        """
        if type(value) != int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """
        Property to retrieve the value of height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Property setter. To set it;
        height must be an integer, otherwise raise TypeError.
        if height is < 0, raise ValueError.
        """
        if type(value) != int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """
        Public instance method that returns the rectangle area
        """
        return self.__height * self.__width

    def perimeter(self):
        """
        Public instance method that returns the rectangle perimeter
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return (self.__height + self.__width) * 2

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        returns the biggest rectangle based on the area
        """
        if isinstance(rect_1, Rectangle) is not True:
            raise TypeError("rect_1 must be an instance of Rectangle")
        if isinstance(rect_2, Rectangle) is not True:
            raise TypeError("rect_2 must be an instance of Rectangle")
        dictr = {rect_1: rect_1.area(), rect_2: rect_2.area()}
        if dictr[rect_1] == dictr[rect_2]:
            return rect_1
        else:
            return max(dictr, key=dictr.get)
