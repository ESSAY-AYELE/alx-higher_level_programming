#!/usr/bin/python3
""" Write an empty class BaseGeometry.

    You are not allowed to import any module"""


class BaseGeometry:
    """ class represents Base geometry"""

    def area(self):
        """ rasie exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ validate value"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value < 1:
            raise ValueError("{} must be greater than 0".format(name))
