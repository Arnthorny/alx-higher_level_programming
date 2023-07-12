#!/usr/bin/python3
"""
This module contains the to_json_string function

Syntax:
    to_json_string(my_obj)
"""

import json


def to_json_string(my_obj):
    """
    Function that returns the JSON represantaton of an object

    Arguments:
        my_obj(:`object`): Object to be serialized

    Returns:
        A string containing the JSON representation
    """

    return (json.dumps(my_obj))
