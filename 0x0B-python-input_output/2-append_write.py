#!/usr/bin/python3
"""the function append"""


def append_write(filename="", text=""):
    """appends a string (UTF8)"""
    with open(filename, "a+", encoding="UTF-8") as f:
        return(f.write(text))
