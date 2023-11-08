#!/usr/bin/python3
""" fuction check if object is like a class"""


def is_same_class(obj, a_class):
    """ the function isinstance of a class"""
    if type(obj) is a_class:
        return True
    return False
