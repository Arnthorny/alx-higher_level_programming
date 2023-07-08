#!/usr/bin/python3
"""
This module contains the matrix_divided function

Syntax:
    matrix_divided(matrix, div)
This function divides all elements of a matrix and rounds
the elements to two decimal places
"""


def matrix_divided(matrix=None, div=None):
    """
    This function divides all elements of a matrix

    Args:
        matrix(:object:`list`): The matrix to be divided
        div(int or float): The divisor

    Raises:
        TypeError if matrix is not a list of lists of integer or floats
        TypeError if rows of matrix are of different sizes
        ZeroDivisionError if div == 0
        TypeError if div is not a number

    Returns:
        The new matrix after the division
    """
    if matrix is None or div is None:
        raise TypeError("Function takes exactly 2 arguments")
    elif type(div) not in (int, float):
        raise TypeError("div must be a number")
    elif div == 0:
        raise ZeroDivisionError("division by zero")

    new_l = []
    len_rows = 0
    i = 0

    for i in range(len(matrix)):
        row = matrix[i]
        if type(row) != list:
            raise TypeError("matrix must be a matrix "
                            "(list of lists) of integers/floats")
        if i == 0:
            len_rows = len(row)
        elif len_rows != len(row):
            raise TypeError("Each row of the matrix must have the same size")

        new_l.append([0] * len_rows)
        for j in range(len(row)):
            if type(row[j]) not in (int, float):
                raise TypeError("matrix must be a matrix "
                                "(list of lists) of integers/floats")
            new_l[i][j] = round(row[j] / div, 2)
    return new_l
