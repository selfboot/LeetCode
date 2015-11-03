#! /usr/bin/env python
# -*- coding: utf-8 -*-


class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        len_n = len(nums)
        start_white = 0
        start_blue = len_n - 1
        for i in range(len_n):
            if i > start_blue:
                break
            if nums[i] == 0:
                nums[i], nums[start_white] = nums[start_white], nums[i]
                start_white += 1
                continue

            while nums[i] == 2:
                if i == start_blue:
                    break
                nums[i], nums[start_blue] = nums[start_blue], nums[i]
                start_blue -= 1

            if nums[i] == 0:
                nums[i], nums[start_white] = nums[start_white], nums[i]
                start_white += 1
