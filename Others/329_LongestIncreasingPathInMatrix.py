#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: xuezaigds@gmail.com


class Solution(object):
    def longestIncreasingPath(self, matrix):
        """
        According to:
        https://leetcode.com/discuss/81747/python-solution-memoization-dp-288ms
        1. Do DFS from every cell
        2. Compare every 4 direction and skip unmatched cells.
        3. Get matrix max from every cell's max
        4. Use matrix[x][y] <= matrix[i][j] so we don't need a visited[m][n] array
        The key is to cache the distance because it's frequently to revisit a cell
        """
        def dfs(i, j):
            if not dp[i][j]:
                val = matrix[i][j]
                dp[i][j] = 1 + max(
                    dfs(i - 1, j) if i and val > matrix[i - 1][j] else 0,
                    dfs(i + 1, j) if i < M - 1 and val > matrix[i + 1][j] else 0,
                    dfs(i, j - 1) if j and val > matrix[i][j - 1] else 0,
                    dfs(i, j + 1) if j < N - 1 and val > matrix[i][j + 1] else 0)
            return dp[i][j]

        if not matrix or not matrix[0]:
            return 0
        M, N = len(matrix), len(matrix[0])
        dp = [[0] * N for i in range(M)]
        return max(dfs(x, y) for x in range(M) for y in range(N))

"""
[[]]
[[3,4,5],[3,2,6],[2,2,1]]
[[9,9,4],[6,6,8],[2,1,1]]
"""
