#! /usr/bin/env python
# -*- coding: utf-8 -*-


class Solution(object):
    # Not notoriously hard-to-understand algorithm KMP
    def strStr(self, haystack, needle):
        # Return 0 if needle is ""
        if not needle:
            return 0
        length = len(haystack)

        # If one char in haystack is same with needle[0],
        # then verify the other chars in needle.
        for i in range(length-len(needle)+1):
            if haystack[i:i+len(needle)] == needle:
                return i

        return -1

"""
""
""
"abaa"
"aa"
"aaabbb"
"abbb"
"""
