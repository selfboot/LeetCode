#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: xuezaigds@gmail.com
# @Last Modified time: 2016-04-04 17:39:46


class Solution(object):
    # Easy to understand.  Refer to
    # https://leetcode.com/discuss/32204/simple-c-solution-8ms-13-lines
    def longestPalindrome(self, s):
        if not s:
            return ""
        s_len = len(s)
        if s_len == 1:
            return s
        max_start, max_end = 0, 1   # Make sure s[start:end] is palindrome
        i = 0
        while i < s_len:
            # No need to check the remainming, pruning here
            if max_end - max_start >= (s_len-i) * 2 - 1:
                break
            left, right = i, i+1
            # Skip duplicate characters i.
            while right < s_len and s[right-1] == s[right]:
                right += 1
            i = right
            while left-1 >= 0 and right < s_len and s[left-1] == s[right]:
                left -= 1
                right += 1
            if right-left > max_end-max_start:
                max_start = left
                max_end = right
        return s[max_start:max_end]

"""
""
"a"
"aa"
"dcc"
"aaaa"
"cccd"
"ccccdc"
"abcdefead"
"""
