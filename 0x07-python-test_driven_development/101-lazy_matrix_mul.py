#!/usr/bin/python3
"""
This module contains the lazy_matrix_mul,
and check_matrices function
Syntax:
    lazy_matrix_mul(m_a, m_b)
    check_matrices(m_a, m_b)

The `matrix_mul` multiplies 2 matrices together
using the numpy module

The check_matrices function checks that both matrix
pass some requirement checks

"""


import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """
    This function returns the product of matrix m_a and m_b.

    Args:
        m_a(:object:`list`): The first matrix
        m_b(:object:`list`): The second matrix

    Raises:
        TypeError if either m_a or m_b is not a list
        ValueError if either m_a or m_b is empty
        ValueError if m_a and m_b can't be multiplied

    Returns:
        The product of m_a and m_b
    """
    if type(m_a) != list:
        raise TypeError("m_a must be a list")
    elif type(m_b) != list:
        raise TypeError("m_b must be a list")
    elif len(m_a) == 0:
        raise ValueError("m_a can't be empty")
    elif len(m_b) == 0:
        raise ValueError("m_b can't be empty")
    elif (check_matrices(m_a, "m_a") != check_matrices(m_b, "m_b")):
        raise ValueError("m_a and m_b can't be multiplied")

    new_mat = np.matmul(m_a, m_b)
    return (new_mat)


def check_matrices(matrix, m_name):
    """
    This function checks that given matrix meet certain.
    requirement checks

    Args:
        matrix(:object:`list`): Matrix
        m_name(:object:`str`): Name of matrix

    Raises:
        TypeError if matrix is not a list of lists
        ValueError if matrix is empty
        TypeError if matrix contain rows of unequal size
        TypeError if matrix contains a value other than integers or floats

        Returns:
            Length of column or row(depending on its name) of given matrix

    """
    len_rows = 0
    for i in range(len(matrix)):
        row = matrix[i]
        if type(row) != list:
            raise TypeError("{} must be a list of lists".format(m_name))
        elif not all(type(el) in (int, float) for el in row):
            raise TypeError(f"{m_name} should contain only integers or floats")

        if i == 0:
            len_rows = len(row)
        elif len_rows != len(row):
            raise TypeError(f"each row of {m_name} must be of the same size")

    if len_rows == 0:
        raise ValueError("{} can't be empty".format(m_name))
    elif m_name == "m_a":
        return len_rows
    else:
        return len(matrix)
