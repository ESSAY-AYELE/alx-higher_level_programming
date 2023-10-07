#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if my_list:
        length = len(my_list)
        if length <= idx or idx < 0:
            return my_list.copy()
        new_list = my_list.copy()
        new_list[idx] = element
        return new_list
