#!/usr/bin/python3
"""Square class"""


class Square:
    """define class"""

    def __init__(self, size=0):
        """initilization Square size"""
        self.__size = size

    @property
    def size(self):
        """to retrieve it"""
        return self.__size

    @size.setter
    def size(self, value):
        """size must be int, if size is less than 0"""

        if type(value) != int:
            raise TypeError("size must be an integer")

        if value < 0:
                raise ValueError("size >= 0")

        self.__size = value

    def area(self):
            """calculate the area"""

            return (self.__size * self.__size)
