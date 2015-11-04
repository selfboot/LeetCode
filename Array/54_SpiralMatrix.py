#! /usr/bin/env python
# -*- coding: utf-8 -*-


class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix:
            return []

        m_row = len(matrix)
        n_col = len(matrix[0])
        min_m_n = min(m_row, n_col)

        spiral_order = []
        step = 0
        while step < (min_m_n + 1) / 2:
            horizontal_len = n_col - 1 - 2 * step
            vertical_len = m_row - 1 - 2 * step
            # print "step.._ |", step, horizontal_len, vertical_len

            # Add the current up edge to spiral order.
            if vertical_len == 0 and horizontal_len > 0:
                horizontal_len += 1
            for i in range(horizontal_len):
                spiral_order.append(matrix[step][i + step])

            # Add the current right edge to spiral order.
            if horizontal_len == 0 and vertical_len > 0:
                vertical_len += 1
            for i in range(vertical_len):
                spiral_order.append(matrix[i + step][n_col - 1 - step])

            if vertical_len > 0:
                # Add the current down edge to spiral order.
                for i in range(horizontal_len):
                    spiral_order.append(
                        matrix[m_row - 1 - step][n_col - 1 - step - i])

            if horizontal_len > 0:
                # Add the current left edge to spiral order.
                for i in range(vertical_len):
                    spiral_order.append(
                        matrix[m_row - 1 - step - i][step])

            step += 1

        # For N * N matrix, where N is an odd number.
        if vertical_len == horizontal_len == 0 and m_row == n_col:
            spiral_order.append(matrix[m_row / 2][n_col / 2])

        return spiral_order


"""
[]
[[1]]
[[1,2,3],[4,5,6],[7,8,9],[10,11,12],[13,14,15]]
[[1],[2],[3]]
[[2,5],[8,4],[0,-1]]
[[1,2,3,4,5,6,7,8,9,10],[11,12,13,14,15,16,17,18,19,20]]
"""
