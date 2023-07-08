#!/usr/bin/python3
"""
This module contains the say_my_name function

Syntax:
        say_my_name(first_name, last_name)
This function prints the string,
"My name is <first_name> <last_name>
"""


def say_my_name(first_name=None, last_name=""):
    """
    This function prints a particular string to stdout

    Args:
        first_name (:object:`string`): The firstname
        last_name (:object:`string`): The lastname
        defaulted to an empty string.

    Raises:
        TypeError if either first_name or last_name is not a string
    """
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    elif type(last_name) is not str:
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
