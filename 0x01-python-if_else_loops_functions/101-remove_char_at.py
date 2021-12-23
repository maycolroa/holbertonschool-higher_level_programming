#!/usr/bin/python3
def remove_char_at(string, i):
    if (i >= 0):
        return string[:i] + string[i + 1:]
    else:
        return string
