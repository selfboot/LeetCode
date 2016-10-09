#! /usr/bin/env python
# -*- coding: utf-8 -*-


class Solution(object):
    def minimumTotal(self, triangle):
        """
        dp[i][j] is the j-th position's minimum path sum in i-th row.
        Then we can find the recursive formula:
            dp[i][j] = min(dp[i-1][j-1] if j-1>=0, dp[i-1][j]) + triangle[i][j]
        """

        if not triangle or not triangle[0]:
            return 0
        rows = len(triangle)
        dp = [0 for i in xrange(rows)]

        for lines in triangle:
            # Scan from tail to head to reduce space, otherwise we need a
            # rows*rows array.
            for j in xrange(len(lines) - 1, -1, -1):
                if (j - 1 >= 0 and dp[j - 1] < dp[j]) or j == len(lines) - 1:
                    dp[j] = dp[j - 1] + lines[j]
                else:
                    dp[j] += lines[j]

        return min(dp)


"""
[]
[[-10]]
[[2],[3,4],[6,5,7],[1,4,8,3]]
[[2],[3,3],[1,5,0],[4,6,9,3]]
"""
