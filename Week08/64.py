#! /usr/bin/env python
# -*- coding: utf-8 -*-


class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid:
            return 0

        m_row = len(grid)
        n_col = len(grid[0])

        # dp[i][j]: minimizes the sum of all numbers
        # along path from top left [0, 0] to [i, j].
        dp = [[0 for i in range(n_col)] for j in range(m_row)]
        dp[0][0] = grid[0][0]

        for row in range(m_row):
            if row > 0:
                dp[row][0] = dp[row-1][0] + grid[row][0]

            for col in range(1, n_col):
                min_pre = dp[row][col-1]
                if row > 0 and dp[row-1][col] < min_pre:
                    min_pre = dp[row-1][col]

                dp[row][col] = min_pre + grid[row][col]

        return dp[m_row-1][n_col-1]

"""
[]
[[0]]
[[1,2,4,3,2,1,5],[3,4,1,2,3,5,4],[3,2,4,5,1,2,5]]
"""
