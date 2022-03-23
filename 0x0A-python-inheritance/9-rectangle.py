#!/usr/bin/python3
"""define class"""


class BaseGeometry:
    """Declare a Rectangle based"""

    pass

    def area(self):
        """Area"""

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """function"""
        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))


class Rectangle(BaseGeometry):

    def __init__(self, width, height):
        """__init__"""
        self.integer_validator("width", width)
        self.__width = width

        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """area"""
        return self.__width * self.__height

    def __str__(self):
        """__str__"""
        return("[Rectangle] {}/{}".format(self.__width, self.__height))
