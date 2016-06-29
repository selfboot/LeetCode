#! /usr/bin/env python
# -*- coding: utf-8 -*-


class Solution(object):
    def uniquePaths(self, m, n):
        # Dynamic Programming.
        # dp[i][j]: present unique paths from (0, 0) to (i-1, j-1)
        dp = [[1 for i in range(n)] for j in range(m)]
        for row in range(1, m):
            for col in range(1, n):
                dp[row][col] = dp[row - 1][col] + dp[row][col - 1]

        return dp[m - 1][n - 1]


class Solution_2(object):
    def uniquePaths(self, m, n):
        """ Using formula.

        Choose (n - 1) movements(number of steps to the right) from (m + n - 2),
        and rest (m - 1) is (number of steps down).
        We calculate the total possible path number
        Combination(N, k) = n! / (k!(n - k)!)
        reduce the numerator and denominator and get
        C = ( (n - k + 1) * (n - k + 2) * ... * n ) / k!
        """
        N, K = m + n - 2, min(n, m) - 1
        path_cnts = 1
        for i in xrange(1, K + 1):
            path_cnts = path_cnts * (N - K + i) / i

        return path_cnts

"""
0
5
3
8
87
99
"""
