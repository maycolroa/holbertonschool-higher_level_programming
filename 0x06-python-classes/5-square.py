#!/usr/bin/python3
"""Square class """


class Square:
    """define class"""

    def __init__(self, size=0):
        """initilization size"""
        self.__size = size

    @property
    def size(self):
        """to recover"""
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

    def my_print(self):
        """prints in stdout the character #"""
        if self.__size is 0:
            print()
        for j in range(self.__size):
            print("#" * self.__size)
