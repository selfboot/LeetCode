#! /usr/bin/env python
# -*- coding: utf-8 -*-


class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        # Return 0 if needle is ""
        if not needle:
            return 0
        length = len(haystack)

        # If one char in haystack is same with needle[0],
        # then verify the other chars in needle.
        for i in range(length):
            if haystack[i] == needle[0]:
                j = i
                for char in needle:
                    if j < length and haystack[j] == char:
                        j += 1
                    else:
                        break
                if j - i == len(needle):
                    return i
            i += 1

        return -1
