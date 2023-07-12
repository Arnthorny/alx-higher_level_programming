#!/usr/bin/python3
"""
This program adds all arguments in argv to a Python list and saves
them all to a file.

"""
import json
import os
import sys
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file


def main():
    """
    Entry point to program
    """
    file = "add_item.json"
    just_created = 0 if os.path.exists(file) else 1
    tmp_list = []

    with open(file, f"{'w' if just_created else 'r+'}", encoding="utf-8") as f:
        if not just_created:
            list_items = json.load(f)
            tmp_list.extend(list_items)
            f.seek(0)
            f.truncate(0)

        tmp_list.extend(sys.argv[1:])
        json.dump(tmp_list, f)


main()
