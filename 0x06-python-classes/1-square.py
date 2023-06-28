#!/usr/bin/python3
"""
This module defines the class Square
based on the 0-square module
"""


class Square:
    """
    A class that defines a square by its size

    Args:
        size (int): Size of each side of "square"

    Attributes:
        __size (int): Size of each side of "square"
    """

    def __init__(self, size):
        self.__size = size
