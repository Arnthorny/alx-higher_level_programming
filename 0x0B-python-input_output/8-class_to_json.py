#!/usr/bin/python3
"""
This module contains the class_to_json function

Syntax:
    class_to_json(obj)
"""


def class_to_json(obj=None):
    """
    Function that returns the dictionary
    description with simple data structure
    for JSON serialization of an object

    Arguments:
        obj(:`object`:): Object to be serialized

    Returns:
        Dictionary description of object
    """
    if hasattr(obj, "__dict__"):
        return (obj.__dict__)
    elif hasattr(obj, "__slots__"):
        new_dict = {x: getattr(obj, x) for x
                    in obj.__slots__ if hasattr(obj, x)}
        return (new_dict)
    else:
        return {}
