#! /usr/bin/env python
# -*- coding: utf-8 -*-


class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if not n:
            return 1

        dp = [0 for i in range(n)]
        dp[0] = 1
        if n > 1:
            dp[1] = 2
        for i in range(2, n):
            dp[i] = dp[i-1] + dp[i-2]

        return dp[n-1]
