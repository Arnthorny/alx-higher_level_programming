#!/usr/bin/python3

"""
This module defines MagicClass that behaves
the same way as a given bytecode
"""


class MagicClass:
    """
    This class implementation, mimics a given bytecode

    Args:
        radius: Radius of given circle

    Attributes:
        __radius: Radius of given circle
    """

    def __init__(self, radius):
        self.__radius = 0
        if ((type(radius) is not int)
                and (type(radius) is not float)):
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """
        Computes area of given square
        Returns:
            The area computed
        """
        return ((self.__radius ** 2) * (math.pi))

    def circumference(self):
        """
        Computes circumference of given square
        Returns:
            The circumference computed
        """
        return (2 * (math.pi) * self.__radius)
