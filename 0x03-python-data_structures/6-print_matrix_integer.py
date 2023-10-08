#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in matrix:
        n = len(i)
        for j in range(n):
            print("{}".format(i[j]), end='')
            if j != n - 1:
                print(' ', end='')
                continue
            print('\n', end='')
