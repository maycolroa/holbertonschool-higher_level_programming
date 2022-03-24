#!/usr/bin/python3

"""define class"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """class Square"""
    def __init__(self, size):
        """subclass"""
        self.integer_validator("size", size)
        self._size = size
        super().__init__(size, size)
