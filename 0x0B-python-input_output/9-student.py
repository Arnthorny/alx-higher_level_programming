#!/usr/bin/python3
"""
This module contains the Student
class that defines a student by first_name,
last_name and age.
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

    def to_json(self):
        """
        This method retrieves the dictionary representation of
        calling object

        Returns:
            Dictionary description of object
        """

        if hasattr(self, "__dict__"):
            return (self.__dict__)
        elif hasattr(self, "__slots__"):
            new_dict = {x: getattr(self, x) for x
                        in self.__slots__ if hasattr(obj, x)}
            return (new_dict)
        else:
            return {}
