#! /usr/bin/env python
# -*- coding: utf-8 -*-


class Solution(object):
    # Binary search.
    def mySqrt(self, x):
        low, high = 0, x
        while low <= high:
            mid = (low + high) / 2
            if mid ** 2 <= x < (mid + 1) ** 2:
                return mid
            elif mid ** 2 > x:
                high = mid - 1
            else:
                low = mid + 1


class Solution_2(object):
    # Newton iterative method
    # According to:
    # http://www.matrix67.com/blog/archives/361
    def mySqrt(self, x):
        if not x:
            return x
        val = x
        sqrt_x = (val + x * 1.0 / val) / 2.0
        while val - sqrt_x > 0.001:
            val = sqrt_x
            sqrt_x = (val + x * 1.0 / val) / 2.0

        return int(sqrt_x)


class Solution_3(object):
    # Shorter Newton method.
    def mySqrt(self, x):
        val = x
        while val * val > x:
            val = (val + x / val) / 2
        return val

"""
0
1
15
90
1010
"""
