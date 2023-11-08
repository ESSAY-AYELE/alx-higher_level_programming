#!/usr/bin/python3
""" Write a class Rectangle that inherits
    from BaseGeometry (7-base_geometry.py).

    Instantiation with width and height
    : def __init__(self, width, height):
    width and height must be private. No getter or setter
    width and height must be positive
    integers, validated by integer_validator """
Base = __import__("7-base_geometry").BaseGeometry


class Rectangle(Base):
    """ a class represent REctangle"""

    def __init__(self, width, height):
        """Intialize a new Rectangle.

        Args:
            width (int): The width of the new Rectangle.
            height (int): The height of the new Rectangle.
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """calcutle the area of rectangle"""
        return (self.__width * self.__height)

    def __str__(self):
        """ string formating for the class"""
        return ("[{}] {}/{}".format
                (self.__class__.__name__, self.__width, self.__height))
