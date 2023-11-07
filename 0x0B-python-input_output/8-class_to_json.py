#!/usr/bin/python3
""" Prototype: def class_to_json(obj):
    obj is an instance of a Class
    You are not allowed to import any module"""


def class_to_json(obj):
    """describtion"""
    return obj.__dict__
