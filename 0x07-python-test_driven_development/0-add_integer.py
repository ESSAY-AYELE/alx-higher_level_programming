#!/usr/bin/python3
""" A function add two intgers"""


def add_integer(a, b=98):
    """ add two intgers that a, b

    a and b  first casted to integers if they are float

    Return:
           the addition of a and b
    rasies:
            TypeError and ValueError
    """
    if type(a) not in (int, float):
        raise TypeError("a must be an integer")
    if type(b) not in (int, float):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
