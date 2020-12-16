#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for fila in range(len(matrix)):
        for elem in range(len(matrix[fila])):
            if elem == len(matrix[fila]) - 1:
                print("{:d}".format(matrix[fila][elem]), end="")
            else:
                print("{:d}".format(matrix[fila][elem]), end=" ")
        print()
