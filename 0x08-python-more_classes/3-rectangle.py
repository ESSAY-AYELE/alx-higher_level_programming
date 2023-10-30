#!/usr/bin/python3
""" Rectangle class """


class Rectangle:
    """ represent a rectangle """
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        """ getter method for width"""
        return self.__width

    @width.setter
    def width(self, value):
        """ setter method for width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ getter for height"""
        return self.__height

    @height.setter
    def height(self, value):
        """ setter method for height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ compute the area of rectangle"""
        return (self.height * self.width)

    def perimeter(self):
        """ compute the perimeter of a rectangle """
        p = 0
        if self.width != 0 and self.height != 0:
            p = 2 * self.width + 2 * self.height
        return (p)

    def __str__(self):
        """Return the printable representation of the Rectangle.

        Represents the rectangle with the # character.
        """
        r = []
        if self.__width == 0 or self.__height == 0:
            return ("")
        for i in range(self.height):
            r.append("#" * self.width)
            if i != self.height - 1:
                r.append("\n")
        return ("".join(r))
