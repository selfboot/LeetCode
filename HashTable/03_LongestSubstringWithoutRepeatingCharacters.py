#! /usr/bin/env python
# -*- coding: utf-8 -*-


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        max_length = 0
        start = 0   # Start index of the substring without repeating characters
        end = 0     # End index of the substring without repeating characters
        char_dict = {}

        for index in range(len(s)):
            char = s[index]
            # Find out a repeating character. So reset start and end.
            if char in char_dict and start <= char_dict[char] <= end:
                start = char_dict[char] + 1
                end = index
            # char is not in the substring already, add it to the substring.
            else:
                end = index
                if end - start + 1 > max_length:
                    max_length = end - start + 1
            char_dict[char] = index

        return max_length

"""
""
"bbbbb"
"abcabcbb"
"""
