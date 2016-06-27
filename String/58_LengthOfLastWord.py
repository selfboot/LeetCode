#! /usr/bin/env python
# -*- coding: utf-8 -*-


class Solution(object):
    def lengthOfLastWord(self, s):
        s = s.strip()
        length = 0
        while length < len(s) and s[-(length + 1)] != " ":
            length += 1

        return length


class Solution_2(object):
    def lengthOfLastWord(self, s):
        return len(s.strip().split(' ')[-1])

"""
""
"are"
"we are teams"
"we are teams    "
"""
