#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    new_matrix = []
    for row in range(len(matrix)):
        new_row = []
        for column in range(len(matrix[row])):
            new_row.append(matrix[row][column] ** 2)
        new_matrix.append(new_row)
    return new_matrix
