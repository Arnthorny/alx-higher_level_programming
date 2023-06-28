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
        return self.__size * self.__size

    @property
    def size(self):
        """int: Getter to get the value of size"""
        return self.__size

    @size.setter
    def size(self, value):
        if ((type(value) != int) and (type(value) != float)):
            raise TypeError("size must be a number")
        elif (value < 0):
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def __eq__(self, oth):
        """Method to define equality operator"""
        if self.area() == oth.area():
            return (True)

    def __ne__(self, oth):
        """Method to define the != operator"""
        if self.area() != oth.area():
            return (True)

    def __gt__(self, oth):
        """Method to define the > operator"""
        if self.area() > oth.area():
            return (True)

    def __ge__(self, oth):
        """Method to define the >= operator"""
        if self.area() >= oth.area():
            return (True)

    def __lt__(self, oth):
        """Method to define the < operator"""
        if self.area() < oth.area():
            return (True)

    def __le__(self, oth):
        """Method to define the <= operator"""
        if self.area() <= oth.area():
            return (True)
