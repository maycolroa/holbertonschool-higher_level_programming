#!/usr/bin/python3
"""Square class"""


class Square:
    """define class"""

    def __init__(self, size=0):
        """initilization Square size"""

        if type(size) != int:
            raise TypeError("size must be an integer")

        if size < 0:
                raise ValueError("size must be >= 0")

        self.__size = size
