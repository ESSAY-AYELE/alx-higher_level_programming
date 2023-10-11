#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    maxval = float('-inf')
    maxkey = None
    for i in a_dictionary.keys():
        if a_dictionary.get(i) > maxval:
            maxval = a_dictionary.get(i)
            maxkey = i
    return maxkey
