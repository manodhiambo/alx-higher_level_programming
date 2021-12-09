#!/usr/bin/python3
"""
A function that divides all elements of a matrix
All elements of the matrix should be divided by div, rounded to 2 decimal places
Returns a new matrix
"""


def matrix_divided(matrix, div):
     """
    A function that divides all elements of a matrix.
    """
    m = "matrix must be a matrix (list of lists) of integers/floats"

    if not (matrix or isinstance(matrix, list)):
        raise TypeError(m)
    if not (isinstance(div, int) or isinstance(div, float)):
        raise TypeError("div must be a number")
    if (div == 0):
        raise ZeroDivisionError("division by zero")
    for row in matrix:
        if (len(row) == 0):
            raise TypeError(m)
        if (len(row) != len(matrix[0])):
            raise TypeError("Each row of the matrix must have the same size")
        if not (row or isinstance(row, list)):
            raise TypeError(m)
        for col in row:
            if not (isinstance(col, int) or isinstance(col, float)):
                raise TypeError(m)
    new_matrix = [[round((col / div), 2) for col in row] for row in matrix]
    return (new_matrix)
