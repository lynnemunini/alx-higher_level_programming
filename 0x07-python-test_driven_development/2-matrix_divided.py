#!/usr/bin/python3

"""
Function that divides all elements of a matrix.
"""


def matrix_divided(matrix, div):

    """
    matrix must be a list of lists of integers or floats,
    otherwise TypeError exception raised with the message matrix
    must be a matrix (list of lists) of integers/floats.
    ================================
    Each row of the matrix must be of the same size, otherwise
    TypeError exception is raised with the message
    Each row of the matrix must have the same size.
    ================================
    div must be a number (integer or float), otherwise TypeError
    exception with the message div must be a number
    ================================
    div can’t be equal to 0, otherwise ZeroDivisionError exception
    with the message division by zero
    ================================
    Elements of the matrix divided by div and rounded to 2 decimal
    places
    """

    if type(matrix) != list or any(isinstance(i, list) for i in matrix) is False:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    for i in matrix:
        for j in i:
            if type(j) != int and type(j) != float:
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    lst = iter(matrix)
    length = len(next(lst))
    if not all(len(i) == length for i in lst):
        raise TypeError("Each row of the matrix must have the same size")

    if type(div) != int and type(div) != float:
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = []
    for i in matrix:
        row = []
        for j in i:
            val = round((j / div), 2)
            row.append(val)
        new_matrix.append(row)

    return new_matrix
