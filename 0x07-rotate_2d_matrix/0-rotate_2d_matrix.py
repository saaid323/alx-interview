#!/usr/bin/env python3
'''Rotate 2D Matrix'''


def rotate_2d_matrix(matrix):
    '''rortates matrix'''
    for i in range(len(matrix)):
        for j in range(i, len(matrix[0])):
            matrix[j][i], matrix[i][j] = matrix[i][j], matrix[j][i]
    for i in range(len(matrix)):
        matrix[i] = matrix[i][::-1]
