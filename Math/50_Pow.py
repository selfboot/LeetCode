#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: xuezaigds@gmail.com
# @Last Modified time: 2016-06-26 20:08:14


class Solution(object):
    def myPow(self, x, n):
        abs_half = abs(n) / 2

        if n == 0:
            return 1.00

        elif n > 0:
            result = self.myPow(x * x, abs_half)
            if n & 1 == 1:
                result *= x
            return result

        else:
            result = 1 / self.myPow(x * x, abs_half)
            if abs(n) & 1 == 1:
                result *= 1 / x
            return result

"""
8.88023
3
2
1
2.2
-100
"""
