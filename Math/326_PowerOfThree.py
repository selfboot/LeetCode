#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: xuezaigds@gmail.com


class Solution(object):
    def isPowerOfThree(self, n):
        # 3 ** 19 = 1162261467
        return n > 0 and not (1162261467 % n)

"""
-1
0
1
27
72
"""
