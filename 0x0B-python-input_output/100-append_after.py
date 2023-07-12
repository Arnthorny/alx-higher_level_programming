#!/usr/bin/python3
"""
This module contains the
append_after function
"""


def append_after(filename="", search_string="", new_string=""):
    """
    This function inserts a line of text to a file, after
    each line containing a specific striing

    Args:
        filename(str): Name of the file to replace
        search_string(str): String to be searched
        new_string(str): String to be replaced
    """

    all_lines = []
    with open(filename, "r", encoding="utf-8") as f:
        for line in f:
            all_lines.append(line)
            if line.find(search_string) != -1:
                all_lines.append(new_string)

    with open(filename, "w", encoding="utf-8") as f:
        f.writelines(all_lines)
