#!/usr/bin/python3
"""
This module contains the class Rectangle
which inherits BaseGeometry of 7-base_geometry module
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
