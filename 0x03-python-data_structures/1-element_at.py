#!/usr/bin/python3
def element_at(my_list, idx):
    lenght = len(my_list)
    if lenght < idx or idx < 0:
         return None
    return my_list[idx]
