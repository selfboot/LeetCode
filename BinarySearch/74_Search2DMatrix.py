#! /usr/bin/env python
# -*- coding: utf-8 -*-


class Solution(object):
    # Don't treat it as a 2D matrix, just treat it as a sorted list
    def searchMatrix(self, matrix, target):
        if not matrix:
            return False

        # Classic binary search: O(logmn)
        m_rows, n_cols = len(matrix), len(matrix[0])
        left, right = 0, m_rows * n_cols - 1

        while left <= right:
            mid = (left+right) / 2
            num = matrix[mid / n_cols][mid % n_cols]
            if num > target:
                right = mid - 1
            elif num < target:
                left = mid + 1
            else:
                return True

        return False

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
