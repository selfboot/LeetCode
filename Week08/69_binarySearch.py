#! /usr/bin/env python
# -*- coding: utf-8 -*-


class Solution(object):
    def mySqrt(self, x):

        left = 0
        right = x
        mid = (left + right) / 2
        while left < right:
            if mid ** 2 > x:
                right = mid - 1
            elif mid ** 2 < x:
                left = mid + 1
            else:
                return mid
            mid = (left + right) / 2
        if left ** 2 > x:
            left -= 1
        return left

"""
0
1
15
90
1010
"""
