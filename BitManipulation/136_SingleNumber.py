#! /usr/bin/env python
# -*- coding: utf-8 -*-


class Solution(object):
    def singleNumber(self, nums):
        num = nums[0]
        for i in nums[1:]:
            num = num ^ i
        return num

"""
[1]
[1,2,3,4,4,3,2]
"""
