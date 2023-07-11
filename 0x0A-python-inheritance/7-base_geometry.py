#!/usr/bin/python3

"""
This module contains the class BaseGeometry
that is based on 6-base_geometry
"""


class BaseGeometry:
    """
    A BaseGeometry class
    """

    def area(self):
        """
        This function raises an exception
        upon its calling.

        Raises:
            Exception always
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value=None):
        """
        This methods validates value and raises an exception if value
        does not meet certain requirements

        Args:
            name(:object: `string`): Name of argument
            value(:`object`: `integer`): Integer to be checked

        Raises:
            TypeError if value is not an integer.
            Valuerror if value is less than or equals 0
        """

        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        elif value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
