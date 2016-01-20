#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: xuezaigds@gmail.com


class Solution(object):
    def summaryRanges(self, nums):
        nums.append("#")      # Guard
        range_str = []
        start, end = nums[0], nums[0]
        for i in xrange(1, len(nums)):
            if nums[i] == nums[i-1] + 1:
                end += 1
            else:
                if start == end:
                    range_str.append(str(start))
                else:
                    range_str.append(str(start) + "->" + str(end))
                start = end = nums[i]
        return range_str

"""
[]
[-1]
[0,1,2,3,5,8,9,11]
"""
