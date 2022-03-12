#!/usr/bin/python3
'''Attributes and Methods'''


def inherits_from(obj, a_class):
    '''returns True if the object'''
    if issubclass(obj.__class__, a_class) and type(obj) != a_class:
        return True
    else:
        return False
