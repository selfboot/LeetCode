#! /usr/bin/env python
# -*- coding: utf-8 -*-


class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        removed_end = 0
        for num in nums:
            if num != val:
                nums[removed_end] = num
                removed_end += 1

        return removed_end
