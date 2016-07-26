#! /usr/bin/env python
# -*- coding: utf-8 -*-


class Solution(object):
    def isMatch(self, s, p):
        """ Dynamic Programming

        dp[i][j] represents isMatch(p[0...i-1], s[0...j-1]), default is False;
        dp[i][0]: isMatch(p[0...i], ""), dp[0][j]: isMatch("", s[0...j])
        dp[0][0] represents

        If p[i] is "*", dp[i+1][j+1] =
            1. dp[i][j+1]        # * matches 0 element in s;
            2. dp[i][j]          # * matches 1 element in s;
            3. dp[i+1][j]        # * matches more than one in s.
        """
        if not s:
            if p.count('*') != len(p):
                return False
            return True

        # Optimized for the big data.
        if len(p) - p.count('*') > len(s):
            return False

        # Initinal process
        dp = [[False for col in range(len(s) + 1)] for row in range(len(p) + 1)]
        dp[0][0] = True     # isMatch("", "") = True
        for i in range(len(p)):
            dp[i + 1][0] = dp[i][0] and p[i] == '*'

        for i in range(len(p)):
            for j in range(len(s)):
                if p[i] == "*":
                    dp[i + 1][j + 1] = dp[i][j + 1] or dp[i][j] or dp[i + 1][j]
                else:
                    dp[i + 1][j + 1] = dp[i][j] and (p[i] == s[j] or p[i] == "?")

        return dp[len(p)][len(s)]

"""
"aa"
"a"
"aa"
"aa"
"aaa"
"aa"
"aa"
"*"
"aa"
"a*"
"ab"
"?*"
"aab"
"c*a*b"
"""
