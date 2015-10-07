#! /usr/bin/env python
# -*- coding: utf-8 -*-


class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        left = 0
        right = len(nums) - 1
        index = -1
        while left <= right:
            mid = (left + right) / 2
            if target == nums[mid]:
                index = mid
                break

            elif target > nums[mid]:
                left = mid + 1

            else:
                right = mid - 1
        if index == -1:
            return [-1, -1]

        start = end = 0
        find_s = False
        find_e = False
        while not find_s or not find_e:
            if index - start >= 0 and nums[index - start] == target:
                start += 1
            else:
                find_s = True

            if index + end <= len(nums) - 1 and nums[index + end] == target:
                end += 1
            else:
                find_e = True

        return [index - start + 1, index + end - 1]
