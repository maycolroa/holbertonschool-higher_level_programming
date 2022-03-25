#!/usr/bin/python3
"""the function"""
from sys import argv


save_from_json = __import__('5-save_to_json_file').save_to_json_file
load_from_json = __import__('6-load_from_json_file').load_from_json_file

filename = "add_item.json"

try:
    counter = load_from_json_file(filename)
except:
    counter = []

save_from_json(counter + argv[1:], filename)
