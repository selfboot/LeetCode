#! /usr/bin/env python
# -*- coding: utf-8 -*-


class Solution(object):
    def numTrees(self, n):
        if not n:
            return 1
        dp = [0 for i in range(n + 1)]
        dp[0] = dp[1] = 1
        for i in range(2, n + 1):
            dp[i] += dp[i - 1] * 2
            # Get the symmetric left and right childs
            for j in range(1, (i - 2) / 2 + 1):
                dp[i] += dp[j] * dp[i - 1 - j] * 2

            # Get the mid one whitout symmetry.
            if (i - 2) % 2 != 0:
                mid_once = (i - 1) / 2
                dp[i] += dp[mid_once] * dp[i - 1 - mid_once]

        return dp[n]

"""
0
1
3
15
"""
