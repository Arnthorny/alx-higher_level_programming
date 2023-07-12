#!/usr/bin/python3

"""
This module contains the pascal_triangle
funtion
"""


def pascal_triangle(n):
    """
    This function returns a list of lists of integers
    representing the Pascal's triangle of n.

    Arguments:
        n(int): Size of Pascal triangle

    Returns:
        List of lists containg triangle else empty list if n<=0
    """

    if (n <= 0):
        return []

    base = [1]
    tmp_base = []
    triangle = []

    for i in range(n):
        tmp_base = []
        for j in range(i + 1):
            if (j == 0 or j == i):
                tmp_base.append(base[0])
            else:
                tmp_base.append(base[j - 1] + base[j])

            # Pascal triangle repeats after each half
            if i % 2 and j == int(i / 2):
                tmp_base.extend(tmp_base[j + 1::-1])
                break
            elif i and i % 2 == 0 and j == int(i / 2):
                tmp_base.extend(tmp_base[j - 1::-1])
                break

        triangle.append(tmp_base)
        base = tmp_base[:]

    return triangle
