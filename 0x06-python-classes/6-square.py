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
        position (:obj:`tuple`, optional): "Coords" to print square

    Attributes:
        __size (int): Size of each side of "square"
        __position (tuple): Position to start printing square
    """

    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

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
            print("\n" * self.__position[1], end='')
            for i in range(self.__size):
                print(" " * self.__position[0], end='')
                print("#" * self.__size)

    @property
    def position(self):
        """tuple: Getter to get the value of position

        The setter raises a TypeError if value passed is not
        a tuple containing exactly 2 positive numbers
        """
        return self.__position

    @position.setter
    def position(self, value):
        try:
            if (type(value) == tuple and value[0] >= 0
                    and value[1] >= 0 and type(value[0]) == int
                    and type(value[1]) == int):
                self.__position = value
            else:
                raise Exception
        except Exception:
            raise TypeError("position must be a tuple of 2 positive integers")
