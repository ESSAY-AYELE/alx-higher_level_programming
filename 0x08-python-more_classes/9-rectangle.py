#!/usr/bin/python3
""" Rectangle class """


class Rectangle:
    """ represent a rectangle """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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
            [r.append(str(self.print_symbol)) for j in range(self.width)]
            if i != self.height - 1:
                r.append("\n")
        return ("".join(r))

    def __repr__(self):
        """ return the the string representation of the Rectangle."""
        return (f"Rectangle({self.width}, {self.height})")

    def __del__(self):
        """what will be run when the object is deleted"""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """that returns the biggest rectangle based on the are"""
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        """returns a new Rectangle instance with width == height == size"""
        return cls(size, size)
