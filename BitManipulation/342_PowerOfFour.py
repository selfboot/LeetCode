#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: xuezaigds@gmail.com
# @Last Modified time: 2016-07-04 17:47:17


class Solution(object):
    """
    Easy to find that power of 4 numbers have those 3 common features.
    First, greater than 0.
    Second, only have one '1' bit in their binary notation.
    Third, the only '1' bit should be locate at the odd location.
    """
    def isPowerOfFour(self, num):
        return bool(num > 0 and num & (num - 1) == 0 and num & 0x55555555)

"""
1
16
256
1000
"""
