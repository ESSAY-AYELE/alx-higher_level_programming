#!/usr/bin/python3
""" compute pascal triangle"""


def pascal_triangle(n):
    """ the function fo pascal triangle  useing recursion"""
    if n == 1:
        return [[1]]
    if n < 1:
        return []
    if n == 2:

        return ([[1], [1, 1]])
    result = []
    result.extend(pascal_triangle(n - 1))
    tmp = result[-1][:]
    tmp2 = [1]*n
    for i in range(len(tmp) - 1):
        tmp2[i + 1] = tmp[i] + tmp[i + 1]
    result.append(tmp2)
    return result
