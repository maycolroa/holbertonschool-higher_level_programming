#!/usr/bin/python3
"""Write an class
"""


class BaseGeometry:
    """Class that defines a shape
    """

    pass

    def area(self):
        """Calculates Area
        """

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """function valide type object
        """
        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """Class BaseGeometry
    """

    def __init__(self, width, height):
        """Initializes the subclass
        """
        self.integer_validator("width", width)
        self.__width = width

        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """return area of rectangule
        """
        return self.__width * self.__height

    def __str__(self):
        """define description a rectangule
        """
        return("[Rectangle] {}/{}".format(self.__width, self.__height))
