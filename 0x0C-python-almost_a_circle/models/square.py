#!/usr/bin/python3
"""
This module contains the Square class.

This class inherits from the
Rectangle class in models.rectangle
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    This class describes a Square object.

    Arguments:
        size(:obj:`int`): Size of square
        x (:obj:`int`, optional): x-coordinate for rectangle
        y (:obj:`int`, optional): y-coordinate for rectangle
        id(:obj:`int`, optional): Id for instance created
    """

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """int: Getter to get the value of width"""
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def __str__(self):
        """
        Returns a nicely formatted string
        representation for the Square instance
        """
        return "[Square] ({}) {}/{} - {}".format(self.id,
                                                 self.x,
                                                 self.y, self.width)

    def update(self, *args, **kwargs):
        """
        Function to update values of instantiated Square object
        """
        allArgs = ("id", "size", "x", "y")

        if args and len(args) > 0:
            for i in range(len(args)):
                if i >= len(allArgs):
                    return
                setattr(self, allArgs[i], args[i])
            return

        for key, value in kwargs.items():
            if hasattr(self, key):
                setattr(self, key, value)

    def to_dictionary(self):
        """
        This method computes the dictionary representation of a Square object.
        Returns:
            dict: Representation
        """
        allArgs = ("id", "size", "x", "y")

        new_dict = {}

        for key in allArgs:
            new_dict[key] = getattr(self, key)

        return new_dict
