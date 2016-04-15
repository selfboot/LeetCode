#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: xuezaigds@gmail.com


class Solution(object):
    def isUgly(self, num):
        for p in [2, 3, 5]:
            while num and num % p == 0:
                num /= p
        return num == 1

"""
-2147483648
1
0
14
8
"""
