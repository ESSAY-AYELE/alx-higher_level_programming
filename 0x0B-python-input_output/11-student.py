#!/usr/bin/python3
""" Write a class Student that defines a student by:

    Public instance attributes:
        first_name
        last_name
        age
    Instantiation with first_name, last_name and age:
    def __init__(self, first_name, last_name, age):
    Public method def to_json(self): that retrieves a dictionary
    representation of a Student instance (same as 8-class_to_json.py)
    You are not allowed to import any module"""


class Student:
    """ student class that represents"""

    def __init__(self, first_name, last_name, age):
        """ init method"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, atrrb=None):
        """retireves a dictionary the instance"""
        if (isinstance(atrrb, list)):
            if all(isinstance(i, str) for i in atrrb):
                return {key: getattr(self, key)
                        for key in atrrb if hasattr(self, key)}
        return self.__dict__

    def reload_from_json(self, json):
        """ set the attr form json"""
        for k, v in json.item():
            setattr(self, k, v)
