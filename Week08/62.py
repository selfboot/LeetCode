#! /usr/bin/env python
# -*- coding: utf-8 -*-


class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        if not m or not n:
            return 0
        # dp[i][j] unique paths from (0, 0) to (i-1, j-1)
        dp = [[0 for i in range(n)] for j in range(m)]
        for row in range(m):
            dp[row][0] = 1
            for col in range(1, n):
                dp[row][col] = dp[row][col-1]
                if row - 1 >= 0:
                    dp[row][col] += dp[row-1][col]

        return dp[m-1][n-1]

"""
0
5
3
8
87
99
"""
