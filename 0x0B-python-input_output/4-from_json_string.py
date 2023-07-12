#!/usr/bin/python3
"""
This module contains the from_json_string function

Syntax:
    from_json_string(my_str)
"""
import json


def from_json_string(my_str):
    """
    Function that returns the an object represented by a JSON string

    Arguments:
        my_str(str): String to be deserialized

    Returns:
        A python data structure(object)
    """

    return (json.loads(my_str))
