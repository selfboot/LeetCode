#! /usr/bin/env python
# -*- coding: utf-8 -*-


class Solution(object):
    def titleToNumber(self, s):
        base = 1
        s_list = list(s)[::-1]
        column = 0
        for char in s_list:
            column += (ord(char)-64) * base
            base *= 26

        return column

"""
""
"A"
"ZZ"
"AAACCCDDD"
"""
