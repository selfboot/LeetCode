#! /usr/bin/env python
# -*- coding: utf-8 -*-


class Solution(object):
    def minPathSum(self, grid):
        if not grid:
            return 0

        m_row = len(grid)
        n_col = len(grid[0])

        # dp[i][j]: the min sum along path from top left to [i,j].
        dp = [[0 for i in range(n_col)] for j in range(m_row)]

        for row in range(m_row):
            for col in range(n_col):
                dp[row][col] = grid[row][col]
                if row == 0 and col > 0:
                    dp[row][col] += dp[row][col - 1]
                elif row > 0 and col == 0:
                    dp[row][col] += dp[row - 1][col]
                elif row > 0 and col > 0:
                    dp[row][col] += min(dp[row - 1][col], dp[row][col - 1])
                else:
                    pass

        return dp[m_row - 1][n_col - 1]


"""
[]
[[0]]
[[1,2,4,3,2,1,5],[3,4,1,2,3,5,4],[3,2,4,5,1,2,5]]
"""
