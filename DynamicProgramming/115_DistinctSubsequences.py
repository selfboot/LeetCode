#! /usr/bin/env python
# -*- coding: utf-8 -*-


class Solution(object):
    def numDistinct(self, s, t):
        """
        dp[i][j] is the number of ways to remove some characters
        from S[0,i] to get T[0,j], we have the recursive formula:
        dp [i][j] = dp[i-1][j] if S[i] != T[j] ,
        or dp [i][j] = dp[i-1][j] + dp[i-1][j-1] if S[i] ==T[j]
        """
        if not s or not t:
            return 0

        s_l, t_l = len(s), len(t)
        if s_l < t_l or (s_l == t_l and s != t):
            return 0

        dp = [0 for i in range(t_l + 1)]
        dp[0] = 1

        for i in xrange(1, s_l + 1):
            # dp[i][j] refer to only dp[i-1][j] and dp[i-1][j-1].
            # This gives us the idea that we can reduce the space to O(n).
            # Since we need to make use of dp[i-1][j-1], we run backward!!!
            for j in xrange(t_l, 0, -1):
                if s[i - 1] == t[j - 1]:
                    dp[j] += dp[j - 1]
        return dp[t_l]

        """Readable, but take O(m*n) space
        dp = [[0 for j in range(t_l+1)] for i in range(s_l+1)]
        dp[0][0] = 1
        for i in xrange(s_l+1):
            dp[i][0] = 1

        for i in xrange(1, s_l+1):
            for j in xrange(1, t_l+1):
                dp[i][j] = dp[i-1][j]
                if s[i-1] == t[j-1]:
                    dp[i][j] += dp[i-1][j-1]
        return dp[s_l][t_l]
        """


"""
""
"a"
"ababcc"
"abc"
"rabbbit"
"rabbit"
"""
