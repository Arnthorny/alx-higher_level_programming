#!/usr/bin/python3
"""
This module contains a class
LockedClass with no class or object attribute.
"""


class LockedClass:
    """This class lets its instances to have an
    called first_name only else it raises an
    AttributeError.
    """
    __slots__ = 'first_name',
