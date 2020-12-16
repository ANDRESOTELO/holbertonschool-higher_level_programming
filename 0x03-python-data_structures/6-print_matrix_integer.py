#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix:
        for x in range(len(matrix)):
            for y in range(len(matrix[x])):
                if y == len(matrix[x]) - 1:
                    print("{:d}".format(matrix[y][x]), end="")
                else:
                    print("{:d}".format(matrix[y][x]), end=" ")
            print()
