#! /usr/bin/env python
# -*- coding: utf-8 -*-


class Solution(object):
    def convertToTitle(self, n):
        title = []
        while n:
            if n % 26 == 0:
                title.insert(0, "Z")
                n -= 26
            else:
                title.insert(0, chr(n % 26 + 64))
            n = n / 26

        return "".join(title)

"""
0
1
52
130
99999999
"""
