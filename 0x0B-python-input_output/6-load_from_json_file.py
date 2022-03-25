#!/usr/bin/python3
"""the function json"""
import json


def load_from_json_file(filename):
    """Creates an Object from a “JSON file"""
    with open(filename, 'r') as file:
        j_file = file.read()
        file.close()
        return json.loads(j_file)
