#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: xuezaigds@gmail.com
# @Last Modified time: 2016-07-08 10:41:44


class Solution(object):
    """
    Let dp[k]: count of numbers with unique digits with length equals k.

    Then:
    f(1) = 10, ...,
    f(k) = 9 * 9 * 8 * ... (9 - k + 2)
    [The first factor is 9 because a number cannot start with 0].

    The problem is asking for numbers from 0 to 10^n.
    Hence return f(1) + f(2) + .. + f(n)
    """
    def countNumbersWithUniqueDigits(self, n):
        if n == 0:
            return 1
        if n == 1:
            return 10
        if n == 2:
            return 91

        dp = [0] * (n + 1)
        dp[1] = 10
        dp[2] = 81

        result = 91
        for i in range(3, min(n + 1, 11)):
            dp[i] = dp[i - 1] * (11 - i)
            result += dp[i]

        return result

"""
0
2
9
12
"""
