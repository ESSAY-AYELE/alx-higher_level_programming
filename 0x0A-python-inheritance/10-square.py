#!/usr/bin/python3
""" Write a class Square that inherits from Rectangle (9-rectangle.py):

    Instantiation with size: def __init__(self, size)::
        size must be private. No getter or setter
        size must be a positive integer, validated by integer_validator
    the area() method must be implemented"""
rec = __import__("9-rectangle").Rectangle


class Square(rec):
    " class that represent a square"""

    def __init__(self, size):
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """compute the area of square"""
        return (self.__size ** 2)

    def __str__(self):
        """ stirng formating"""
        return ("[Rectangle] {}/{}".format(self.__size, self.__size))
