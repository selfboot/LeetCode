#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: xuezaigds@gmail.com
# Refer to
# https://leetcode.com/discuss/38489/easy-solution-with-detailed-explanations-8ms-time-and-space


class Solution(object):
    """
    Dynamic Programming.
    dp[row][col]: the maximal side length of the square
    that can be achieved at point (i, j)
    For i > 0 and j > 0:
        if matrix[i][j] = 0, P[i][j] = 0;
        if matrix[i][j] = 1 (Think it over until you get it)
        P[i][j] = min(P[i - 1][j], P[i][j - 1], P[i - 1][j - 1]) + 1.
    """
    def maximalSquare(self, matrix):
        if not matrix:
            return 0
        m_rows = len(matrix)
        n_cols = len(matrix[0])

        # Initinal
        dp = [[0 for col in range(n_cols)] for row in range(m_rows)]
        dp[0] = [int(matrix[0][j]) for j in range(n_cols)]
        max_area = int(max(dp[0]))
        for row in range(1, m_rows):
            for col in range(n_cols):
                if not col:
                    dp[row][col] = int(matrix[row][col])
                elif matrix[row][col] == "0":
                    dp[row][col] = 0
                else:
                    dp[row][col] = min(
                        dp[row-1][col],
                        dp[row][col-1],
                        dp[row-1][col-1]) + 1
                max_area = max(max_area, dp[row][col] ** 2)
        return max_area

"""
# Solution 2: Similar to 85. Maximal Rectangle
class Solution(object):
    def maximalSquare(self, matrix):
        if not matrix:
            return 0
        m_rows = len(matrix)
        n_cols = len(matrix[0])
        max_area = 0

        # Pre process the matrix.
        pro_matrix = [[0 for col in range(n_cols)] for row in range(m_rows)]
        for i in range(m_rows):
            for j in range(n_cols):
                if not i:
                    pro_matrix[i][j] = int(matrix[i][j])
                else:
                    num = 1 if matrix[i][j] == "1" else 0
                    pro_matrix[i][j] = (pro_matrix[i-1][j] + num) * num
            max_area = max(max_area, self.largestSquareArea(pro_matrix[i]))

        return max_area

    def largestSquareArea(self, height):
        height.append(0)
        size = len(height)
        no_decrease_stack = [0]
        max_size = 0

        i = 0
        while i < size:
            cur_num = height[i]
            if (not no_decrease_stack or
                    cur_num > height[no_decrease_stack[-1]]):
                no_decrease_stack.append(i)
                i += 1
            else:
                index = no_decrease_stack.pop()
                if no_decrease_stack:
                    width = i - no_decrease_stack[-1] - 1
                else:
                    width = i
                max_size = max(max_size, min(width, height[index]) ** 2)

        return max_size
"""

"""
[]
["1"]
["01"]
["00", "00"]
["10100", "10111", "11111"]
"""
