#! /usr/bin/env python
# -*- coding: utf-8 -*-


class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        len_w1 = len(word1)
        len_w2 = len(word2)

        # dp[i][j]: minimum number of steps convert word1[0,i) to word2[0,j)
        dp = [[0 for j in range(len_w2+1)] for i in range(len_w1+1)]

        # initial the dp array
        dp[0][0] = 0
        for j in range(1, len_w2+1):
            dp[0][j] = j
        for i in range(1, len_w1+1):
            dp[i][0] = i

        for i in range(1, len_w1+1):
            for j in range(1, len_w2+1):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min(
                        dp[i-1][j-1] + 1,
                        dp[i-1][j] + 1,
                        dp[i][j-1] + 1,)

        return dp[len_w1][len_w2]
