#! /usr/bin/env python
# -*- coding: utf-8 -*-


class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        m = len(obstacleGrid)
        if not m:
            return 0
        n = len(obstacleGrid[0])

        # dp[i][j] unique paths from (0, 0) to (i-1, j-1)
        dp = [[0 for i in range(n)] for j in range(m)]
        for row in range(m):
            if row == 0:
                dp[row][0] = 1 - obstacleGrid[0][0]
            if row - 1 >= 0:
                if obstacleGrid[row][0] == 0:
                    dp[row][0] = dp[row-1][0]
                else:
                    dp[row][0] = 0
            for col in range(1, n):
                if obstacleGrid[row][col] == 1:
                    dp[row][col] = 0
                    continue
                dp[row][col] = dp[row][col-1]
                if row - 1 >= 0:
                    dp[row][col] += dp[row-1][col]

        return dp[m-1][n-1]

"""
[[0]]
[[0,0,0],[0,1,0],[0,0,0]]
[[0,0,0,0],[0,0,1,1],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
[[1],[0]]
"""
