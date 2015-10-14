#! /usr/bin/env python
# -*- coding: utf-8 -*-


class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if len(nums) == 1:
            return 0

        last = nums[0]
        step = 1
        index = 1
        while last < len(nums) - 1:
            max_distance = 0
            while index <= last:
                if nums[index] + index > max_distance:
                    max_distance = nums[index] + index
                index += 1

            last = max_distance
            step += 1

        return step
