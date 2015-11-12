#! /usr/bin/env python
# -*- coding: utf-8 -*-


class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        removed_end = 0
        for i in range(1, len(nums)):
            if nums[i] != nums[removed_end]:
                removed_end += 1
                nums[removed_end] = nums[i]

        return removed_end + 1

"""
[]
[1,1,2,2,3]
[1,3,5,8,9,9,9]
"""
