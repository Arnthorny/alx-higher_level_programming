#!/usr/bin/python3
"""
This module contains the write_file function

Syntax:
    write_file(filename="", text="")
"""


def write_file(filename="", text=""):
    """
    Function that writes a string to a file referenced by `filename`
    and returns the number of characters written

    Arguments:
        filename(:`object`:`string`): Name of file to be written to
        text(:`object`:`string`): String to be written to file
    """

    with open(filename, "w", encoding="utf-8") as f:
        no_of_chars = f.write(text)
        return (no_of_chars)
