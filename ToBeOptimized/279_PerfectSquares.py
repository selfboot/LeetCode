#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: xuezaigds@gmail.com


# Dynamic Programming with static variable
class Solution(object):
    # Since dp is a static vector, we have already calculated the result
    # during previous function calls and we can just return the result now.
    _dp = [0]

    def numSquares(self, n):
        dp = self._dp
        while len(dp) <= n:
            i = len(dp)
            min_count = 2 ** 31 - 1
            for j in range(1, int(i**0.5) + 1):
                min_count = min(min_count, dp[i-j*j]+1)
            dp.append(min_count)
        return dp[n]


# Dynamic Programming
# Easy to undersrtand but unfortually "Time Limit Exceeded"
class Solution_2(object):
    def numSquares(self, n):
        dp = [0] * (n+1)
        for i in range(1, n+1):
            min_count = 2 ** 31 - 1
            for j in range(1, int(i**0.5) + 1):
                min_count = min(min_count, dp[i-j*j]+1)
            dp[i] = min_count
        return dp[n]

"""
1
12
13
156
"""
