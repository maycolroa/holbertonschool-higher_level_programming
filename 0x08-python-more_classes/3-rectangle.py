#!/usr/bin/python3
"""Defines a Rectangle class."""


class Rectangle:
    """Rectangle class"""

    def __init__(self, width=0, height=0):
        """Initializes a Rectangle instance"""
        self.width = width
        self.height = height

    def __str__(self):
        """Returns an informal of a Rectangle instance"""
        if self.__height == 0 or self.__width == 0:
            return ''
        rec_str = ''
        for i in range(self.__height):
            for j in range(self.__width):
                rec_str += '#'
            rec_str += '\n'
        return rec_str[:-1]

    @property
    def width(self):
        """Retrieves the width of a Rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the width of a Rectangle"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Retrieves the height of a Rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the height of a Rectangle"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Calculates the area of a Rectangle Area of the the rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """Calculates the perimeter of a Rectangle
            Perimeter of the rectangle"""
        if self.__height == 0 or self.__width == 0:
            return 0
        return 2 * (self.__width + self.__height)
