#!/usr/bin/python3
def append_to_list(matrix=[]):

    new_list = []
    if len(matrix) == 0:
        return new_list

    for row in matrix:
        for value in row:
            new_list.append(value)

    return new_list

