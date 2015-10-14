#! /usr/bin/env python
# -*- coding: utf-8 -*-


class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        A[i][j] -----> A[j][n-1-i]
        Firstly, A[i][j] --> A[j][i]
        Then,    A[j][i] --> B[j][n-1-i]
        """

        length = len(matrix)
        for i in range(length):
            for j in range(i):
                temp = matrix[i][j]
                matrix[i][j] = matrix[j][i]
                matrix[j][i] = temp

        for i in range(length):
            for j in range(length/2):
                temp = matrix[i][length-1-j]
                matrix[i][length-1-j] = matrix[i][j]
                matrix[i][j] = temp
