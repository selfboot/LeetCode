#! /usr/bin/env python
# -*- coding: utf-8 -*-


class Solution(object):
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        if not s1:
            if s2 == s3:
                return True
            else:
                return False
        s1_l = len(s1)
        s2_l = len(s2)
        s3_l = len(s3)
        if s3_l != s1_l + s2_l:
            return False

        # dp[i][j] is true when s3[i+j-1] is formed by the interleaving of
        # s1[:i](previous i chars of s1) and s2[:j](previous j chars of s2).
        dp = [[False for j in xrange(s2_l+1)] for i in xrange(s1_l+1)]
        dp[0][0] = True

        for i in xrange(1, s1_l+1):
            if s1[i-1] == s3[i-1]:
                dp[i][0] = True
            else:
                break

        for j in xrange(1, s2_l+1):
            if s2[j-1] == s3[j-1]:
                dp[0][j] = True
            else:
                break

        for i in xrange(1, s1_l+1):
            for j in xrange(1, s2_l+1):
                if (s1[i-1] == s3[i+j-1] and dp[i-1][j] or
                        s2[j-1] == s3[i+j-1] and dp[i][j-1]):
                    dp[i][j] = True

        return dp[s1_l][s2_l]

"""
""
"a"
"a"
"aa"
"ab"
"abaa"
"aabcc"
"dbbca"
"aadbbbaccc"
"aaaabbbb"
"ddaacccc"
"addaacaaabbbcccb"
"""
