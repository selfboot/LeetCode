#! /usr/bin/env python
# -*- coding: utf-8 -*-


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        max_length = 0
        start = 1
        end = 1
        index = 1
        char_dict = {}

        for char in s:
            if char in char_dict and start <= char_dict[char] < end:
                start = char_dict[char] + 1
                end = index + 1
            else:
                end = index + 1
                if end - start > max_length:
                    max_length = end - start

            char_dict[char] = index
            index = index + 1

        return max_length
