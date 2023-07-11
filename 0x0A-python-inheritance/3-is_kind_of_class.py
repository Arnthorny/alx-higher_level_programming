#!/usr/bin/python3

"""
This module contains the is_kind_of_class
function
"""


def is_kind_of_class(obj, a_class):
    """
    This function returns True if obj is an instance of
    or if the obj is an instance of a class that
    inherited from the specified class.
    Otherwise False.
    Returns:
        True or False
    """

    return (isinstance(obj, a_class))
