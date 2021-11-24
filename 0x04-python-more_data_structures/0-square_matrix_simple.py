#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    for i in matrix:
        temp_list = list(map(lambda x: x * x, i))
        new_matrix.append(temp_list)
        return (new_matrix)
