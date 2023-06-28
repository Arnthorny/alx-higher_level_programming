#!/usr/bin/python3
"""
This module defines the class Square
based on the 4-square module
"""


class Square:
    """
    A class that defines a square by its size,
    raises a ValueError if size is < 0
    othewise raises a TypeError if size is not an int.

    Args:
        size (:obj:`int`, optional): Size of each side of "square"

    Attributes:
        __size (int): Size of each side of "square"
    """

    def __init__(self, size=0):
        self.size = size

    def area(self):
        """
        Computes area of given square
        Returns:
            The area computed
        """
        return(self.__size * self.__size)

    @property
    def size(self):
        """int: Getter to get the value of size"""
        return(self.__size)

    @size.setter
    def size(self, value):
        if (type(value) != int):
            raise TypeError("size must be an integer")
        elif (value < 0):
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def my_print(self):
        """
        Prints out the given square to stdout with # character
        Returns:
            None
        """
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                print("#" * self.__size)
