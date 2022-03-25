#!/usr/bin/python3
"""the function write"""


def write_file(filename="", text=""):
    """writes a string (UTF8)"""
    with open(filename, "w", encoding="UTF-8") as f:
        return(f.write(text))
