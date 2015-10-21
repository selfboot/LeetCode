#! /usr/bin/env python
# -*- coding: utf-8 -*-


class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        if len(nums) == 1:
            return True

        last = nums[0]
        index = 1
        if last >= len(nums) - 1:
            return True

        while index <= last:
            max_distance = 0
            while index <= last:
                if nums[index] + index > max_distance:
                    max_distance = nums[index] + index
                index += 1
            last = max_distance

            if last >= len(nums) - 1:
                return True

        return False
