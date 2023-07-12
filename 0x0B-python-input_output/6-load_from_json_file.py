#!/usr/bin/python3
"""
This module contains the load_from_json_file function

Syntax:
    load_from_json_file(filename)
"""
import json


def load_from_json_file(filename):
    """
    Function that creates an Object from a 'JSON file'

    Arguments:
        filename(:`object`: `str`): Name of file to read from
    """

    with open(filename, encoding="utf-8") as f:
        return (json.load(f))
