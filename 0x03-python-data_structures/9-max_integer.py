#!/usr/bin/python3
def max_integer(my_list=[]):
    if not my_list:
        return None
    m = float('-inf')
    for i in my_list:
        if m < i:
            m = i
    return m
