#!/usr/bin/python3
"""
This module contains the matrix_mul,
len_rowOrCol and rowByCol function
Syntax:
    matrix_mul(m_a, m_b)
    len_rowOrCol(matrix, row_or_col)
    rowByCol(row, col)

The `matrix_mul` multiplies 2 matrices together

The `len_rowOrCol` determines the length of the row
or column(depending on 2nd arg) of a given matrix.
It'll also perform some requirement checks

The `rowByCol` multiplies a given row by a given column
and returns the resulting value.
"""


def matrix_mul(m_a=None, m_b=None):
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
    elif (len_rowOrCol(m_a, "col") != len_rowOrCol(m_b, "row")):
        raise ValueError("m_a and m_b can't be multiplied")

    row_sz = len(m_a)
    col_sz = len(m_b[0])

    new_mat = [[0 for i in range(col_sz)] for j in range(row_sz)]
    for i in range(len(new_mat)):
        row = new_mat[i]
        for j in range(len(row)):
            tmp_col = [row[j] for row in m_b]
            new_mat[i][j] = rowByCol(m_a[i], tmp_col)

    return new_mat


def len_rowOrCol(matrix, row_or_col):
    """
    This function computes the size of a matrix's row or column.
    It also performs some checks on the matrix

    Args:
        matrix(:object:`list`): The matrix
        row_or_col(:object:`string`): String to determine if row or col

    Raises:
        TypeError if either m_a or m_b is not a list of lists
        ValueError if either m_a or m_b is empty
        TypeError if either m_a or m_b contain rows of unequal size

    Returns:
        The length of either row or column of matrix
    """

    m_name = "m_a" if row_or_col == "col" else "m_b"

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
    elif row_or_col == "col":
        return len_rows
    else:
        return len(matrix)


def rowByCol(row, col):
    """
    This function computes the product of the row and column
    from matrices m_a and m_b

    Args:
        row(:object:`list`): Row of m_a
        col(:object:`list`): Column of m_b

    Raises:
        TypeError if either row or
        col contains a value other than integers or floats
        ValueError if matrices can't be multiplied

    Returns:
        The product
    """
    sum_val = 0
    if len(row) != len(col):
        raise ValueError("m_a and m_b can't be multiplied")

    for i in range(len(row)):
        if type(row[i]) not in (int, float):
            raise TypeError("m_a should contain only integers or floats")
        elif type(col[i]) not in (int, float):
            raise TypeError("m_b should contain only integers or floats")
        else:
            sum_val += (row[i] * col[i])

    return (sum_val)
