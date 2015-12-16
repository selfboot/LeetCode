#! /usr/bin/env python
# -*- coding: utf-8 -*-


class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        Dynamic Programming
        dp[i]: if s[i:] can be broken to wordDict. then:
        dp[i-1] = s[i:i+k] in wordDict and dp[i+k+1], for all the possible k.
        """
        if not s:
            return True
        if not wordDict:
            return False
        s_len = len(s)
        dp = [False for i in range(s_len+1)]
        dp[-1] = True
        for i in range(s_len-1, -1, -1):
            k = 0
            while k+i < s_len:
                cur_fisrt_word = s[i:i+k+1]
                if cur_fisrt_word in wordDict and dp[i+k+1]:
                    dp[i] = True
                    break
                else:
                    k += 1
        return dp[0]

"""
""
[]
"leetcode"
["leet","code"]
"leetcodecode"
["leet","code"]
"""
