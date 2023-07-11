#!/usr/bin/python3
"""
This module contains the Rectangle
class based on the 8-rectangle module
"""


BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """
    A Rectangle class inheriting from the BaseGeometry class

    Args:
        width(int): The width of the rectangle
        height(int): Height of rectangle
    """

    def __init__(self, width, height):
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """
        This method returns the area of the Rectangle
        object that calls it
        """
        return self.__width * self.__height

    def __str__(self):
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
