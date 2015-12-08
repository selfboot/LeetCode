#! /usr/bin/env python
# -*- coding: utf-8 -*-


def comp(a, b):
    return int(a + b > b + a) * 2 - 1


class Solution(object):
    def largestNumber(self, nums):
        nums = map(str, nums)
        nums.sort(cmp=comp, reverse=True)
        return str(int("".join(nums)))

"""
[1]
[1,2,3,21]
[1,2,3,23]
"""
