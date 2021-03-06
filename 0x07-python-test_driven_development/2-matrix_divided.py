#!/usr/bin/python3
"""Divide matrix members by given number"""


def matrix_divided(matrix, div):
    """Function that divides all elements of a matrix"""

    error = "matrix must be a matrix (list of lists) of integers/floats"
    if type(matrix) is not list:
        raise TypeError(error)
    if len(matrix) == 0:
        raise TypeError(error)
    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if type(matrix[0]) is not list:
        raise TypeError(error)

    div_matrix = []
    row_len = len(matrix[0])
    for row in matrix:
        if type(row) is not list:
            raise TypeError(error)
        if row_len != len(row):
            raise TypeError("Each row of the matrix must have the same size")
        row_list = []
        for element in row:
            if type(element) is not int and type(element) is not float:
                raise TypeError(error)
            row_list.append(round(float(element / div), 2))
        div_matrix.append(row_list)
    return div_matrix
