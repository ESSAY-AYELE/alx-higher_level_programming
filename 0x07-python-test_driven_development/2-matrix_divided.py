#!/usr/bin/python3
""" a Fuction that divide a matrix on a given number"""


def matrix_divided(matrix, div):
    """ a function that divides all elements of a matrix

        raise: TypeError, ZeroDivisionError"""
    if not is_raws_equal(matrix):
        raise TypeError ("Each row of the matrix must have the same size")
    if not is_number(matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if type(div) not in (int, float):
        raise TypeError("div must be a number")
    result = []
    
    for i in matrix:
        raw = []
        for j in i:
            raw.append(round(j / div, 2))
        result.append(raw)
    return (result)

def is_raws_equal(matrix):
    """ a fuction check if a matrix have equal number of raws"""
    prev_raw = len(matrix[0])
    for raw in matrix:
        cur_raw = len(raw)
        if cur_raw != prev_raw:
            return (False)
        prev_raw = cur_raw
    return (True)

def is_number(matrix):
    """ a check every element of a matrix is float or int"""
    for raw in matrix:
        for i in raw:
            if type(i) not in (int, float):
                return (False)
    return(True)
