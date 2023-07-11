#!/usr/bin/python3
"""
This module contains the class Square
based on the 10-square module
"""


Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """
    A Square class inheriting from the Rectangle class

    Args:
        size(int): The size of the square
    """

    def __init__(self, size):
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """
        This method returns the area of the Square
        object that calls it
        """
        return self.__size * self.__size

    def __str__(self):
        return "[Square] {}/{}".format(self.__size, self.__size)
