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

        features = {}
        counter = 0

        if type(attrs) == list:
            for item in attrs:
                if type(item) != str:
                    counter = 1
                    break
                for key, value in self.__dict__.items():
                    if key == item:
                        features[key] = value
            if counter == 0:
                return (features)

        return (self.__dict__)
