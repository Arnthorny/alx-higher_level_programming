#!/usr/bin/python3
"""
This module contains the ``MyList`` class
which contains the method ``print_sorted``.
"""


class MyList(list):
    """
    This class inherits the ``list`` class
    """
    def print_sorted(self):
        """
        This function prints the list specified by self
        but prints in a sorted manner(ascending order),
        without affecing the original list
        """

        print(sorted(self))
