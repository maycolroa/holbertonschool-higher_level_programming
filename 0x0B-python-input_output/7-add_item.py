#!/usr/bin/python3
"""the function Add items """

from os import path
from sys import argv

save_to_json_file = __import__("5-save_to_json_file").save_to_json_file

load_from_json_file = __import__("6-load_from_json_file").load_from_json_file


def add_items():
    """add items"""

    counter = []

    """Check"""
    if path.isfile("add_item.json"):
        counter = load_from_json_file("add_item.json")

    if len(argv) > 1:

        for j in range(1, len(argv)):
            counter.append(argv[j])

    """ Write file """

    save_to_json_file(counter, "add_item.json")


if __name__ == "__main__":
    add_items()
