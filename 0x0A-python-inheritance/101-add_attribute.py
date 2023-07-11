#!/usr/bin/python3

"""
This module contains the add_attribte
function
"""


def add_attribute(obj, key, value):
    """
    This function adds the new attribute to a obj if possible.
    Otherwise it raises a TypeError

    Args:
        obj (:object:`object`): The object.
        key (string): The name of the attribute
        value(object): Value of the attribute

    """

    if (hasattr(obj, "__dict__")):
        obj.__dict__[key] = value
    elif (hasattr(obj, "__setattr__")) and (hasattr(obj, "__slots__")
                                            and (key in obj.__slots__)):
        obj.__setattr__(key, value)
    else:
        raise TypeError("can't add new attribute")
