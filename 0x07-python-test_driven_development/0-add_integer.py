#!/usr/bin/python3
"""
This module contains the add_integer function

Syntax:
    add_integer(a, b=98)
This function raises a TypeError if a or b is not a number
If a or b is a float, it typecasts it to an int before addition
"""


def add_integer(a=None, b=98):
    """
    This function adds two integers together

    Args:
        a(int or float): The first number
        b(int or float): The second number, defaults to 98

    Raises:
        TypeError if either a or b is not an integer or a float
        TypeError if no argument is passed
        OverflowError if infinity is passed

    Returns:
        The sum of a and b
    """
    if a is None:
        raise TypeError("Function requires at least one argument")
    elif type(a) not in (int, float):
        raise TypeError("a must be an integer")
    elif type(b) not in (int, float):
        raise TypeError("b must be an integer")
    elif ((a == float('inf') or a == float('-inf')) or
            (b == float('inf') or b == float('-inf'))):
        raise OverflowError("Cannot cast infinity to int")
    else:
        return (int(a) + int(b))
