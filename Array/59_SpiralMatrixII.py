#! /usr/bin/env python
# -*- coding: utf-8 -*-


class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        if not n:
            return []

        matrix = [[-1 for row in range(n)] for col in range(n)]
        current_num = 1
        step = 0
        while step < n / 2:
            edge_len = n - 1 - 2 * step

            # Get number from left to right(up edge)
            for i in range(edge_len):
                matrix[step][i + step] = current_num
                current_num += 1

            # Get number from up to down(right edge)
            for i in range(edge_len):
                matrix[i + step][n - 1 - step] = current_num
                current_num += 1

            # Get number from right to left(down edge)
            for i in range(edge_len):
                matrix[n - 1 - step][n - 1 - step - i] = current_num
                current_num += 1

            # Get number from down to up(left edge)
            for i in range(edge_len):
                matrix[n - 1 - step - i][step] = current_num
                current_num += 1
            step += 1

        if n % 2 == 1:
            matrix[n/2][n/2] = current_num
        return matrix

"""
0
1
3
4
"""
