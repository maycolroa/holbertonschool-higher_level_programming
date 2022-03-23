#!/usr/bin/python3
"""define class"""


class BaseGeometry:
    """class BaseGeometry"""

    def area(self):
        """area"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """funtion"""
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))

        elif value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
