#!/usr/bin/python3

"""
This module contains the class MyInt
"""


class MyInt(int):
    """
    A class which inherits from int but inverts
    the '==' and '!=' operators
    """
    def __eq__(self, other):
        return super().__ne__(other)

    def __ne__(self, other):
        return super().__eq__(other)
