#!/usr/bin/python3
"""
This module contains the print_square function

Syntax:
        print_square(size)
This function prints a square of given size,
with the '#' character.
"""


def print_square(size=None):
    """
    This function prints a square to stdout

    Args:
        size (:object:`int`): The size of the square.

    Raises:
        TypeError if size is not an integer
        ValueError if size is less than 0.
    """
    if type(size) is not int:
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")
    else:
        square = "#" * size
        for i in range(size):
            print("{}".format(square))
