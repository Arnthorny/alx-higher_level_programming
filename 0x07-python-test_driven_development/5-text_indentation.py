#!/usr/bin/python3
"""
This module contains the text_indentation function

Syntax:
        text_indentation(text)
This function prints a text with 2 new lines after these chars -
'.', ',', and '?'.
"""


def text_indentation(text):
    """
    This function indents a given text and prints it to stdout

    Args:
        text (:object:`string`): The string to be indented.

    Raises:
        TypeError if text is not a string
    """
    if type(text) is not str:
        raise TypeError("text must be a string")
    new_str = ""
    new_line = True
    for i in range(len(text)):
        if (new_line and text[i] == ' '):
            continue
        elif (text[i] in ('.', '?', ':')):
            print(text[i], end="")
            print("\n")
            new_line = True
        else:
            print(text[i], end="")
            new_line = False
