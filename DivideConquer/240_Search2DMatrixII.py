#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: xuezaigds@gmail.com


class Solution(object):
    """
    O(m+n)
    Check the top-right corner.
    If it's not the target, then remove the top row or rightmost column.
    """
    def searchMatrix(self, matrix, target):
        if not matrix or len(matrix[0]) < 1:
            return False
        m, n = len(matrix), len(matrix[0])

        # We start search the matrix from top right corner
        # Initialize the current position to top right corner.
        row, col = 0, n - 1
        while row < m and col >= 0:
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] > target:
                col -= 1
            else:
                row += 1
        return False


class Solution_2(object):
    # O(m+n): same as the pre solution, more efficient and pythonic.
    # According to
    # https://leetcode.com/discuss/47571/4-lines-c-6-lines-ruby-7-lines-python-1-liners
    def searchMatrix(self, matrix, target):
        if not matrix or len(matrix[0]) < 1:
            return False
        n = len(matrix[0])
        col = -1
        for row in matrix:
            while col + n > 0 and row[col] > target:
                col -= 1
            if row[col] == target:
                return True
        return False


class Solution_3(object):
    # O(mn): 1 lines python. Just for fun
    def searchMatrix(self, matrix, target):
        return any(target in row for row in matrix)

"""
[[]]
0
[[-5]]
-2
[[1, 4, 7, 11, 15], [2, 5, 8, 12, 19], [3, 6, 9, 16, 22], [10, 13, 14, 17, 24]]
12
"""
