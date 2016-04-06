#! /usr/bin/env python
# -*- coding: utf-8 -*-


class Solution(object):
    def removeElement(self, nums, val):
        removed_end = 0
        for num in nums:
            if num != val:
                nums[removed_end] = num
                removed_end += 1

        return removed_end

"""
[]
0
[2,2,2,3,3,3,5,5,5]
4
[1,2,3,4,5,1,2,3,4,5]
3
"""
