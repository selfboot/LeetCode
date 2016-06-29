#! /usr/bin/env python
# -*- coding: utf-8 -*-


class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        m = len(obstacleGrid)
        if not m:
            return 0
        n = len(obstacleGrid[0])

        # dp[i][j] unique paths from (0, 0) to (i-1, j-1)
        dp = [[0 for i in range(n + 1)] for j in range(m + 1)]
        dp[0][1] = 1
        for i in xrange(1, m + 1):
            for j in xrange(1, n + 1):
                # If there is a obstacle at (i,j), then dp[i][j] = 0
                if not obstacleGrid[i - 1][j - 1]:
                    dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        return dp[m][n]


"""
[[0]]
[[0,0,0],[0,1,0],[0,0,0]]
[[0,0,0,0],[0,0,1,1],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
[[1],[0]]
"""
