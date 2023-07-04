#!/usr/bin/python3
"""
This module contains the class Rectangle
that defines a rectangle based on 1-rectangle
"""


class Rectangle:
    """A class that defines a rectangle based on its
    width and height.

    Raises a TypeError if width or height is not an integer
    Raises a ValueError if width or height is < 0

    Args:
        width (int): Width of the rectangle instance
        height (int): Height of the rectangle instance

    Attributes:
    __width (int): Width of the rectangle instance
    __height (int): Height of the rectangle instance
    """

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        """This is the width property"""
        return self.__width

    @width.setter
    def width(self, value):
        if (type(value) != int):
            raise TypeError("width must be an integer")
        elif (value < 0):
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """This is the height property"""
        return self.__height

    @height.setter
    def height(self, value):
        if (type(value) != int):
            raise TypeError("height must be an integer")
        elif (value < 0):
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """
        Computes area of given rectangle
        Returns:
            The area computed
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        Computes Perimeter of given rectangle
        Returns:
            The area computed
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)
