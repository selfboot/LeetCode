#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: xuezaigds@gmail.com


class Solution(object):
    def isUgly(self, num):
        while num > 1:
            can_divid = False
            for factor in [2, 3, 5]:
                if num % factor == 0:
                    num /= factor
                    can_divid = True
            if not can_divid:
                return False
        return num == 1

"""
-2147483648
1
0
14
8
"""
