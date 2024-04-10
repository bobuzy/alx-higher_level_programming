#!/usr/bin/python3
"""module definition for matrix_divided"""


def matrix_divided(matrix, div):

    """divides all elements of a matrix.

    Args:
        matrix: the list containing int or float
        div: the number to divide the matrix by

    Raises:
        TypeError: If matrix is not list of lists containing int or float.
        TypeError: If sublists are not all same size.
        TypeError: If div is not int or float.
        ZeroDivisionError: If div is zero.

    Returns:
        the result of the divided matrix
    """

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if not isinstance(matrix, list) or len(matrix) == 0:
        raise TypeError("matrix must be a matrix (list of lists) " +
                        "of integers/floats")

    new_matrix = []

    for row in range(len(matrix)):
        if not isinstance(matrix[row], list) or len(matrix[row]) == 0:
            raise TypeError("matrix must be a matrix (list of lists) " +
                            "of integers/floats")
        if len(matrix[row]) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")

        sub_matrix = []

        for col in range(len(matrix[row])):
            if not isinstance(matrix[row][col], (int, float)):
                raise TypeError("matrix must be a matrix (list of lists) " +
                                "of integers/floats")
            else:
                result = round(matrix[row][col] / div, 2)
                sub_matrix.append(result)

        new_matrix.append(sub_matrix)

    return new_matrix


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/2-matrix_divided.txt")
