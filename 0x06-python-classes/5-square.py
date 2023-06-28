#!/usr/bin/python3

class Square:
    """A class that defines a square by its size"""

    def __init__(self, size=0):
        """Instantiates the data with size"""
        self.size = size

    def area(self):
        """Returns current square area"""
        return(self.__size * self.__size)

    @property
    def size(self):
        """Getter to get the value of size"""
        return(self.__size)

    @size.setter
    def size(self, value):
        """Setter to set the value of size"""
        if (type(value) != int):
            raise TypeError("size must be an integer")
        elif (value < 0):
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def my_print(self):
        """Print the square with the # character"""
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                print("#" * self.__size)
