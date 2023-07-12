#!/usr/bin/python3
"""
This module contains the Student
class that defines a student based on the 9-student module,
"""


class Student:
    """
    A Student class that defines a student

    Arguments:
        first_name(str): The student's first name
        last_name(str): The student's last name
        age(int): The student's age

    Attributes:
        first_name(str): First name
        last_name(str): Last name
        age(int): Student's age
    """

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        This method retrieves the dictionary representation of
        calling object

        Args:
            attrs(:`object`:`list`): List of attribute to retrieve
        Returns:
            Dictionary description of object
        """
        if (type(attrs) == list and (all(type(x) == str for x in attrs))):
            new_dict = {}
            for attr in attrs:
                if hasattr(self, attr):
                    new_dict[attr] = getattr(self, attr)
            return new_dict
        else:
            if hasattr(self, "__dict__"):
                return (self.__dict__)
            elif hasattr(self, "__slots__"):
                new_dict = {x: getattr(self, x) for x
                            in self.__slots__ if hasattr(obj, x)}
                return (new_dict)
            else:
                return {}
