#!/usr/bin/python3
"""
This module contains the ``Base`` class
"""
import json
import os
import csv
import tkinter as tk
from random import randrange as rr


class Base:
    """
    This class will be the 'base' of all other classes

    Arguments:
        id(:obj:`int`, optional): Id for instance created

    Atttributes:
        __nb_objects(int): Counter for number of objects instantiate
    """

    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries=None):
        """
        This function computes the JSON string of a given list of dictionaries.

        Args:
            list_dictionaries(:object:`list`): List of dictionaries

        Returns:
            JSON string if list_dictionaries is valid.
            Else "[]".
        """
        if list_dictionaries is None:
            return "[]"
        elif type(list_dictionaries) != list:
            raise TypeError("list_dictionaries must be a list of dictionaries")
        elif len(list_dictionaries) == 0:
            return "[]"
        elif not all(type(d) == dict for d in list_dictionaries):
            raise TypeError("list_dictionaries must be a list of dictionaries")
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs=None):
        """
        This function writes the JSON string representation
        of a list of objects to a file.

        Args:
            list_objs(:object:`list`): List of instances
                                       who inherit from ``Base`` -
            example: list of ``Rectangles`` or list of ``Square``.

        """
        filename = f"{cls.__name__}.json"
        content = ""
        if list_objs is None:
            content = "[]"
        elif type(list_objs) != list:
            raise TypeError("list_objs must be a list of objects")
        elif not all(type(o) == cls for o in list_objs):
            raise TypeError("list_objs objects must be homogeneous")
        else:
            c_list = list(map(lambda obj: obj.to_dictionary(), list_objs))
            content = cls.to_json_string(c_list)

        if os.path.exists(filename):
            if not os.path.isfile(filename):
                raise TypeError("{} must be a regular file".format(filename))
        with open(filename, "w", encoding="utf-8") as f:
            f.write(content)

    @staticmethod
    def from_json_string(json_string=None):
        """
        This function computes a list from a given JSON string.

        Args:
            json_string(:object:`str`): String to be deserialized

        Returns:
            list: List represented by JSON string.
            Else an empty list.
        """
        if json_string is None or json_string == "":
            return []

        new_list = json.loads(json_string)

        if (type(new_list) != list or not
                all(type(d) == dict for d in new_list)):
            raise TypeError("Deserialized object not list of dictionaries")
        else:
            return new_list

    @classmethod
    def create(cls, **dictionary):
        """
        Function to create a new instance of type cls.

        Args:
            **dictionary: Keyword arguments

        Returns:
            `obj`: A new instance with attributes set from kwargs
        """
        if cls.__name__ == "Square":
            dummy = cls(1)
        else:
            dummy = cls(1, 1)

        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """
        Function to return a list of instance from JSON File

        Returns:
            List of instances or an empty list if file is nonexistent
        """
        filename = f"{cls.__name__}.json"

        if os.path.exists(filename) and not os.path.isfile(filename):
            raise TypeError("{} must be a regular file".format(filename))
        else:
            try:
                with open(filename, "r", encoding="utf-8") as f:
                    json_str = f.read()
                    list_dict = cls.from_json_string(json_str)
            except (FileNotFoundError):
                return []

            instances = list(map(lambda d: cls.create(**d), list_dict))
            return instances

    @classmethod
    def save_to_file_csv(cls, list_objs=None):
        """
        This function writes the CSV string representation
        of a list of objects to a file.

        Args:
            list_objs(:object:`list`): List of instances
                                       who inherit from ``Base`` -
            example: list of ``Rectangles`` or list of ``Square``.

        """
        filename = f"{cls.__name__}.csv"
        if os.path.exists(filename):
            if not os.path.isfile(filename):
                raise TypeError("{} must be a regular file".format(filename))

        if filename == "Rectangle.csv":
            fieldnames = ("id", "width", "height", "x", "y")
        else:
            fieldnames = ("id", "size", "x", "y")

        c_list = []
        if list_objs is None:
            pass
        elif type(list_objs) != list:
            raise TypeError("list_objs must be homogeneous "
                            "list of `Base` objects")
        elif not all(type(o) == cls for o in list_objs):
            raise TypeError("list_objs must be homogeneous "
                            "list of `Base` objects")
        else:
            c_list = list(map(lambda obj: obj.to_dictionary(), list_objs))

        with open(filename, "w", encoding="utf-8", newline='') as f:
            csvWriter = csv.DictWriter(f, fieldnames=fieldnames)
            csvWriter.writerows(c_list)

    @classmethod
    def load_from_file_csv(cls):
        """
        Function to return a list of instance from CSV File

        Returns:
            List of instances or an empty list if file is nonexistent
        """
        filename = f"{cls.__name__}.csv"
        list_dict = []
        if filename == "Rectangle.csv":
            fieldnames = ("id", "width", "height", "x", "y")
        else:
            fieldnames = ("id", "size", "x", "y")

        if os.path.exists(filename) and not os.path.isfile(filename):
            raise TypeError("{filename} must be a regular file")
        else:
            try:
                with open(filename, "r", encoding="utf-8", newline='') as f:
                    csvReader = csv.reader(f)
                    for row in csvReader:
                        if len(row) != len(fieldnames):
                            raise TypeError("Invalid CSV file")
                        try:
                            new_row = [int(x) for x in row]
                            new_dict = {k: v for (k, v) in
                                        zip(fieldnames, new_row)}
                            list_dict.append(new_dict)
                        except (ValueError, TypeError):
                            raise TypeError("Invalid CSV file")
            except (FileNotFoundError):
                return []

        instances = list(map(lambda d: cls.create(**d), list_dict))
        return instances

    @staticmethod
    def draw(list_rectangles, list_squares):
        """
        This function uses the tkinter module to draw rectangles and squares

        Args:
            list_rectangles(list): A list of Rectangle objects
            list_squares(list): A list of Square objects
        """
        if (type(list_rectangles), type(list_squares)) != (list, list):
            raise TypeError("Arguments must be list of Base objs")

        def draw_shape(o):
            def rand_col():
                return f"#{rr(0,256):02x}{rr(0,256):02x}{rr(0,256):02x}"

            canva.create_rectangle(o.x, o.y, o.x+o.width,
                                   o.y+o.height, outline=rand_col(),
                                   fill=rand_col())

        win = tk.Tk()
        win.title("Let's draw it")
        win.geometry("750x600")
        canva = tk.Canvas(win, height=500, width=500, bg='#ffe')
        canva.pack()
        for shape in (list_rectangles + list_squares):
            draw_shape(shape)
        win.mainloop()
