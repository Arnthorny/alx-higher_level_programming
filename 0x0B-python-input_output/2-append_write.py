#!/usr/bin/python3
"""
This module contains the append_write function

Syntax:
    append_write(filename="", text="")
"""


def append_write(filename="", text=""):
    """
    Function that appends a string to end of a text file
    referenced by `filename` and returns the
    number of characters appended

    Arguments:
        filename(:`object`:`string`): Name of file to be written to
        text(:`object`:`string`): String to be appended to file
    """

    with open(filename, "a", encoding="utf-8") as f:
        no_of_chars = f.write(text)
        return (no_of_chars)
