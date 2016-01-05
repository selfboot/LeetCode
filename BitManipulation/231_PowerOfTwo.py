#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: xuezaigds@gmail.com


# Easy to understand.
class Solution(object):
    def isPowerOfTwo(self, n):
        if n <= 0:
            return False
        while n:
            if n & 1 and n != 1:
                return False
            n >>= 1
        return True


# Another solution: using n&(n-1) trick
class Solution_2(object):
    def isPowerOfTwo(self, n):
        return n > 0 and not n & (n-1)

"""
-7
0
1
2
15
121
"""
