#!/usr/bin/python3
"""
This module contains the Rectangle class.
This class inherits from the Base class in models.base
"""
from models.base import Base


class Rectangle(Base):
    """
    This class describes a Rectangle object.

    Arguments:
        width(:obj:`int`): Width of rectangle
        height(:obj:`int`): Height of rectangle
        x (:obj:`int`, optional): x-coordinate for rectangle
        y (:obj:`int`, optional): y-coordinate for rectangle
        id(:obj:`int`, optional): Id for instance created
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """int: Getter to get the value of width"""
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """int: Getter to get the value of height"""
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """int: Getter to get the value of x"""
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) != int:
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """int: Getter to get the value of y"""
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) != int:
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """
        Computes given instance area.

        Returns:
            int: area
        """
        return self.__width * self.__height

    def display(self):
        """
        Prints instance with # character.
        """
        y_pos = "{}".format('\n' * self.__y)
        row = f"{' ' * self.__x}{'#' * self.__width}"
        print(y_pos, end="")
        for i in range(self.__height):
            print(row)

    def __str__(self):
        """
        Returns a nicely formatted string
        representation for the Rectangle instance
        """
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
                                                       self.id,
                                                       self.__x,
                                                       self.__y,
                                                       self.__width,
                                                       self.__height)

    def update(self, *args, **kwargs):
        """
        Function to update values of instantiated Rectangle object
        """
        allArgs = ("id", "width", "height", "x", "y")

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
        This method computes the dictionary representation of a `Rectangle`.
        Returns:
            dict: Representation
        """
        allArgs = ("id", "width", "height", "x", "y")

        new_dict = {}

        for key in allArgs:
            new_dict[key] = getattr(self, key)

        return new_dict
