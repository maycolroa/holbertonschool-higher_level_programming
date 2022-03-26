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

        my__dict__studen = {}
        if attrs is not None:
            return self.__dict__
        for counter in attrs:
            if counter in self.__dict__.keys():
                my_dict[counter] = self.__dict__[counter]
        return my_dict

    def reload_from_json(self, json):
        """Public method that replaces all
        counteributes of the Student instance"""

        my_old_dict = self.__dict__
        for counter in json.keys():
            for my_old_counter in my_old_dict.keys():
                if counter == my_old_counter:
                    my_old_dict[my_old_counter] = json[counter]
            return my_old_dict
