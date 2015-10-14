#! /usr/bin/env python
# -*- coding: utf-8 -*-


class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.

        """

        length = len(matrix)
        new_matrix = [[0 for col in range(length)] for row in range(length)]

        for i in range(length):
            for j in range(length):
                new_matrix[j][length-1-i] = matrix[i][j]

        for i in range(length):
            for j in range(length):
                matrix[i][j] = new_matrix[i][j]
