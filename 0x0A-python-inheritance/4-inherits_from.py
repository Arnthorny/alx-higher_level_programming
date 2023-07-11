#!/usr/bin/python3

"""
This module contains the inherits_from
function
"""


def inherits_from(obj, a_class):
    """
    This function returns True if obj is an instance of
    of a class that inherited (directly or indirectly)
    from specified class

    Otherwise False.
    Returns:
        True or False
    """

    return ((type(obj) != a_class) and (issubclass(type(obj), a_class)))
