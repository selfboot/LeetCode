#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: xuezaigds@gmail.com
# @Last Modified time: 2016-07-04 11:44:22


class Solution(object):
    # Binary Search
    def isPerfectSquare(self, num):
        low, high = 0, num
        while low <= high:
            mid = (low + high) / 2
            if mid ** 2 == num:
                return True
            elif mid ** 2 > num:
                high = mid - 1
            else:
                low = mid + 1
        return False


class Solution_2(object):
    # Truth: A square number is 1+3+5+7+...  Time Complexity O(sqrt(N))
    def isPerfectSquare(self, num):
        i = 1
        while num > 0:
            num -= i
            i += 2
        return num == 0


class Solution_3(object):
    # Newton Method.  Time Complexity is close to constant.
    # According to: https://en.wikipedia.org/wiki/Newton%27s_method
    def isPerfectSquare(self, num):
        val = num
        while val ** 2 > num:
            val = (val + num / val) / 2
        return val * val == num

"""
0
1
121
12321
2147483647
"""
