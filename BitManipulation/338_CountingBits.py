#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: xuezaigds@gmail.com
# @Last Modified time: 2016-04-05 17:18:25


class Solution(object):
    def countBits(self, num):
        """
        f[i] = f[i / 2] + i % 2
        or
        f[i] = f[i&(i-1)] + 1, i&(i-1) drops the lowest set bit
        """
        ans = [0] * (num + 1)
        for i in xrange(1, num + 1):
            ans[i] = ans[i >> 1] + (i & 0x1)
            # ans[i] = ans[i & (i - 1)] + 1
        return ans

"""
0
1
12
"""
