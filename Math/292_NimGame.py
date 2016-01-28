#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: xuezaigds@gmail.com


class Solution(object):
    # Just get the conclusion from the following second way.
    def canWinNim(self, n):
        if n % 4:
            return True
        else:
            return False


class Solution_2(object):
    # Easy to understand, need more memory.
    # Can be optimized by using static variable.
    def canWinNim(self, n):
        dp = [True] * (n+1)
        if n > 3:
            dp[4] = False
            for i in range(5, n+1):
                if dp[i-1] and dp[i-2] and dp[i-3]:
                    dp[i] = False
        return dp[n]

"""
1
8
12
245
12345
"""
