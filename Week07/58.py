#! /usr/bin/env python
# -*- coding: utf-8 -*-


class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0

        while s[-1] == " ":
            s = s[:-1]
            if not s:
                return 0

        length = 0
        while length < len(s) and s[-(length + 1)] != " " :
            length += 1

        return length
