#!/usr/bin/python3
"""the function json"""
import json


def save_to_json_file(my_obj, filename):
    """This function returns the JSON"""
    with open(filename, mode="w", encoding="utf-8") as file:
        json.dump(my_obj, file)
