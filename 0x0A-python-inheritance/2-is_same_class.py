#!/usr/bin/python3

"""
This module contains the is_same_class
function
"""


def is_same_class(obj, a_class):
    """
    This function returns True if obj is exactly
    an instance of the specified class.

    Returns:
        True or False
    """

    return (type(obj) == a_class)
