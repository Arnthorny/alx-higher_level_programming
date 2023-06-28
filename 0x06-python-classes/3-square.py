#!/usr/bin/python3
"""
This module defines the class Square
based on the 2-square module
"""


class Square:
    """
    A class that defines a square by its size,
    raises a ValueError if size is < 0
    othewise raises a TypeError if size is not an int.

    Raise errors if size isn't an intege or is < 0.

    Args:
        size (:obj:`int`, optional): Size of each side of "square"

    Attributes:
        __size (int): Size of each side of "square"
    """

    def __init__(self, size=0):
        if (type(size) != int):
            raise TypeError("size must be an integer")
        elif (size < 0):
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """
        Computes area of given square
        Returns:
            The area computed
        """
        return(self.__size * self.__size)
