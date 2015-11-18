#! /usr/bin/env python
# -*- coding: utf-8 -*-


class Solution(object):

    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s or s[0] == "0":
            return 0

        len_s = len(s)
        # dp[i]: total number of ways to decode s[0:i)
        dp = [1 for i in range(len_s + 1)]
        for i in range(1, len_s):
            pre_num = ord(s[i - 1]) - ord('0')
            cur_num = ord(s[i]) - ord('0')
            num = pre_num * 10 + cur_num

            if cur_num == 0:
                if num > 26 or num == 0:
                    return 0
                else:
                    dp[i+1] = dp[i-1]

            else:
                if num <= 26 and pre_num != 0:
                    dp[i + 1] = dp[i] + dp[i - 1]
                else:
                    dp[i + 1] = dp[i]

        return dp[len_s]

"""
""
"123"
"1238"
"172731349111222"
"0"
"10203"
"""
