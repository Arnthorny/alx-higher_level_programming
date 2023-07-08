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


def lazy_matrix_mul(m_a=None, m_b=None):
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
        new_mat(numpy: array): The product of m_a and m_b
    """

    new_mat = np.matmul(m_a, m_b)
    return (new_mat)
