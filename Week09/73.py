#! /usr/bin/env python
# -*- coding: utf-8 -*-


class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        if not matrix:
            return []

        m = len(matrix)
        n = len(matrix[0])

        # Frist, make sure whether first row and first col is all 0.
        first_row = False
        for i in range(n):
            if matrix[0][i] == 0:
                first_row = True
        first_col = False
        for j in range(m):
            if matrix[j][0] == 0:
                first_col = True

        # Keep the information about the 0 cell to first row and first col.
        for row in range(1, m):
            for col in range(1, n):
                if matrix[row][col] == 0:
                    matrix[row][0] = 0
                    matrix[0][col] = 0

        # Set 0s according to the information in first row and first col
        for row in range(m):
            for col in range(n):
                if not matrix[row][0] or not matrix[0][col]:
                    matrix[row][col] = 0

        # Set the first row and first col
        if first_row:
            for col in range(n):
                matrix[0][col] = 0
        if first_col:
            for row in range(m):
                matrix[row][0] = 0

"""
[[0]]
[[1,0],[2,2]]
[[0,0,0,5],[4,3,1,4],[0,1,1,4],[1,2,1,3],[0,0,1,1]]
"""
