#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: xuezaigds@gmail.com
# @Last Modified time: 2016-07-04 14:00:57


class Solution(object):
    def reverseString(self, s):
        return s[::-1]


class Solution_2(object):
    def reverseString(self, s):
        left, right = 0, len(s) - 1
        s = list(s)
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
        return "".join(s)


"""
""
"hello"
"  HELLO "
"""
