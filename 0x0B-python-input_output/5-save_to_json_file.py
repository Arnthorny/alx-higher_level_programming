#!/usr/bin/python3
"""
This module contains the save_to_json_file function

Syntax:
    save_to_json_file(my_obj, filename)
"""
import json


def save_to_json_file(my_obj, filename):
    """
    Function that write an Object to a text file
    using a JSON representaton of the object

    Arguments:
        my_obj(:`object`): Object to be serialized
        filename(:`object`: `str`): Name of file for writing
    """

    with open(filename, "w", encoding="utf-8") as f:
        json.dump(my_obj, f)
