#!/usr/bin/python3
"""append_after"""


def append_after(filename="", search_string="", new_string=""):
    """search"""

    counter = []
    with open(filename, "r", encoding="utf-8") as f:
        counter = f.readlines()
        intercom = 0

        while intercom < len(counter):
            if search_string in counter[intercom]:
                counter[intercom:intercom + 1] = [counte
                [intercom], new_string]
                intercom += 1
            intercom += 1

    with open(filename, "w", encoding="utf-8") as file:
        file.writelines(counter)
