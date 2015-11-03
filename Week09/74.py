#! /usr/bin/env python
# -*- coding: utf-8 -*-


class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if matrix == [[]]:
            return False

        m_rows = len(matrix)
        n_cols = len(matrix[0])
        left = 0
        right = m_rows * n_cols - 1
        mid = (left + right) / 2
        while left < right:
            row = mid / n_cols
            col = mid - row * n_cols
            current_num = matrix[row][col]
            if current_num > target:
                right = mid - 1
            elif current_num < target:
                left = mid + 1
            else:
                return True
            mid = (left + right) / 2

        return matrix[mid/n_cols][mid-(mid/n_cols)*n_cols] == target

"""
[[]]
0
[[1]]
0
[[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 50]]
34
[[1, 3, 5], [10, 11, 16], [23, 30, 34]]
46
"""
