#!/usr/bin/python3
"""
This module contains the read_file function

Syntax:
    read_file(filename="")
"""


def read_file(filename=""):
    """
    Function to read a file referenced by `filename`
    and print file's content to stdout.

    Arguments:
        filename(:`object`:`string`): Name of file to be read
    """

    with open(filename, encoding="utf-8") as f:
        file_content = f.read()
        print(file_content, end="")
