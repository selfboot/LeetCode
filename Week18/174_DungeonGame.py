#! /usr/bin/env python
# -*- coding: utf-8 -*-


class Solution(object):
    def calculateMinimumHP(self, dungeon):
        """  Dynamic Programming
        dp[i][j]: the leatest health point must remain before enter room [i, j]
        Initinal: After enter the princess's room,
                  knight's health point should at least be 1.
                  that's say, dp[m_rows-1][n_cols-1] = 1 or 1-demon's hurt
        Then assume the knight go from princess's room(right_down) to up_left.

        DP process: There are two ways to enter to room [i, j], dp[i][j] =
                    1. right to left: dp[i][j+1] - dungeon[i][j] or 1
                    2. down to up: dp[i+1][j] - dungeon[i][j] or 1
        """
        m_rows = len(dungeon)
        n_cols = len(dungeon[0])
        dp = [[1 for i in range(n_cols)] for j in range(m_rows)]
        if dungeon[-1][-1] > 0:
            dp[-1][-1] = 1
        else:
            dp[-1][-1] = 1 - dungeon[-1][-1]

        for i in range(m_rows-1, -1, -1):
            for j in range(n_cols-1, -1, -1):
                down_up = None
                right_left = None
                if i+1 < m_rows:
                    if dungeon[i][j] >= dp[i+1][j]:
                        down_up = 1
                    else:
                        down_up = dp[i+1][j] - dungeon[i][j]
                if j+1 < n_cols:
                    if dungeon[i][j] >= dp[i][j+1]:
                        right_left = 1
                    else:
                        right_left = dp[i][j+1] - dungeon[i][j]
                if right_left and down_up:
                    dp[i][j] = min(down_up, right_left)
                elif right_left or down_up:
                    dp[i][j] = down_up or right_left
                else:
                    pass

        return dp[0][0]
"""
[[0]]
[[-1]]
[[0,-3]]
[[-2,-3,-3], [-5,-10,1], [10,30,-5]]
"""
