#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dict = a_dictionary.copy()
    keys = list(new_dict)
    values = new_dict.values()
    num = list(map(lambda x: x * 2, values))
    j = 0
    for i in keys:
        new_dict[i] = num[j]
        j += 1
    return new_dict
