#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = matrix.copy()
    count = len(matrix)
    for x in range(count):
        new_matrix[x] = list(map(lambda x: x**2, matrix[x]))
    return new_matrix
