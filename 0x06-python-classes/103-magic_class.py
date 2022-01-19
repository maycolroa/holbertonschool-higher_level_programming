#!/usr/bin/python3
"""Defines a class"""
import math


class MagicClass:
    """define class"""

    def __init__(self, radius=0):
        """Initializes Class"""
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')
        self.__radius = radius

    def area(self):
        """Calculaes the area"""
        return (self.__radius ** 2) * math.pi

    def circumference(self):
        """Calculates the circumference"""
        return 2 * math.pi * self.__radius
