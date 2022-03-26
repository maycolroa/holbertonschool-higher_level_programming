#!/usr/bin/python3
"""class Student"""


class Student:
    """class Student"""

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """dictionary representation of a Student"""
        if attrs is not None:
            dict_counter = {}
            for j in self.__dict__:
                if j in attrs:
                    dict_counter[j] = self.__dict__[j]
            return dict_counter
        else:
            return self.__dict__

    def reload_from_json(self, json):
        """Replaces all attributes"""
        if json:
            self.__dict__ = json
