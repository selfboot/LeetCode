#! /usr/bin/env python
# -*- coding: utf-8 -*-


class Solution(object):
    def longestValidParentheses(self, s):
        """
        According to:
        https://leetcode.com/discuss/8092/my-dp-o-n-solution-without-using-stack

        dp[i]: the longest length of valid parentheses which ends at i. Then:

        1. s[i] is '(', dp[i] = 0
        2. s[i] is ')'
            a. s[i-dp[i-1]-1] == '(': dp = dp[i-1] + 2 + dp[i-dp[i-1]-2]
            b. dp[i] = 0

        Just think about what does s[i-dp[i-1]-1] == '(' mean.
        """
        if not s:
            return 0

        dp = [0] * len(s)
        max_len = 0
        for i in xrange(1, len(s)):
            if s[i] == ")" and i - 1 - dp[i - 1] >= 0 and s[i - 1 - dp[i - 1]] == "(":
                dp[i] = dp[i - 1] + 2 + dp[i - dp[i - 1] - 2]
                max_len = max(max_len, dp[i])

        return max_len

"""
""
")"
"()"
"))"
"(((()()()))("
"(((()()()))())"
"""
