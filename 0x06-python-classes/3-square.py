#!/usr/bin/python3
"""Square class"""


class Square:
    """define  class"""

    def __init__(self, size=0):
        """initilization size"""

        if type(size) != int:
            raise TypeError("size must be an integer")

        if size < 0:
                raise ValueError("size >= 0")

        self.__size = size

    def area(self):
            """calculate the area"""

            return (self.__size * self.__size)
