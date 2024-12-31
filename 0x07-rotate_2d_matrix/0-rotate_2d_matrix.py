#!/usr/bin/python3
"""
Function that rotates a [nxn] 2D matrix 90 degrees clockwise
"""


def rotate_2d_matrix(matrix):
    """
    Rotate 2D square-matrix clockwise 90degrees
    Args:
        matrix (list): 2D square matrix
    Return:
        None
    """
    length = len(matrix)
    for i in range(length):
        for j in range(i):
            temp = matrix[i][j]
            matrix[i][j] = matrix[j][i]
            matrix[j][i] = temp

    for i in range(length):
        for j in range(int(length / 2)):
            temp = matrix[i][j]
            matrix[i][j] = matrix[i][length-1-j]
            matrix[i][length-1-j] = temp
