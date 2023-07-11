#!/usr/bin/python3

"""
This module contains the lookup
function
"""


def lookup(obj):
    """
    This function returns the list of available attributes
    and methods of an object.

    Returns:
        A list object.
    """

    return (dir(obj))
