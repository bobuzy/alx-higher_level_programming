#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for row in range(len(matrix)):
        for nest in range(len(matrix[row])):
            print("{:d}".format(matrix[rew][nest]), end="")
            if nest != (len(matrix[row]) - 1):
                print(" ", end="")
        print()
