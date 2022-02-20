#!/usr/bin/python3
'''class Rectangle'''


class Rectangle:
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        return self.width * self.__height

    def perimeter(self):
        if self.__height == 0 or self.__width == 0:
            return 0
        per = (2 * self.__height) + (2 * self.__width)
        return per

    def __str__(self):
        if self.__width == 0 or self.__height == 0:
            return ""
        for j in range(self.__height - 1):
            print("#" * self.__width)
        return ("#" * self.__width)
